import random
import string
import uuid
import accounts.auth_backends
from accounts.forms import CustomUserCreationForm
from companies.models import Company
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from .models import PendingUser


# Helper: Username auto-generate
def generate_username(first_name, last_name):
    # Remove spaces from first and last name
    clean_first = first_name.lower().replace(" ", "")
    clean_last = last_name.lower().replace(" ", "")

    base_username = f"{clean_first}{clean_last}"

    suffix = ''.join(random.choices(string.digits, k=4))  # only digits
    username = f"{base_username}{suffix}"  # no special character

    # Ensure username uniqueness
    while User.objects.filter(username=username).exists():
        suffix = ''.join(random.choices(string.digits, k=4))
        username = f"{base_username}{suffix}"

    return username


# Register User View
def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email').lower().strip()
            raw_password = form.cleaned_data.get('password1')



            # 🔐 Hash password for storing safely in PendingUser
            hashed_password = make_password(raw_password)

            # 🎯 Unique token for verification
            token = str(uuid.uuid4())

            # 📝 Save into PendingUser table (NOT User table)
            PendingUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=hashed_password,
                token=token
            )

            # 📩 Build verification link
            verification_link = request.build_absolute_uri(
                reverse('verify-pending-user', args=[token])
            )

            subject = "Verify Your Account"
            html_message = f"""
                <h2>Hello {first_name}!</h2>
                <p>Click the link below to verify your email address:</p>
                <a href="{verification_link}">Verify My Account</a>
                <p>This link will expire in 24 hours.</p>
            """

            try:
                msg = EmailMultiAlternatives(subject, html_message, settings.DEFAULT_FROM_EMAIL, [email])
                msg.attach_alternative(html_message, "text/html")
                msg.send()
                messages.success(request, "A verification link has been sent to your email address.")
            except Exception as e:
                messages.error(request, f"Failed to send verification email: {str(e)}")

            return redirect('register')

    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})



# Email verification vie


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "Your account has been verified successfully!")
        return redirect("create-company")
    else:
        return render(request, 'verification_failed.html')


def check_username(request):
    username = request.GET.get('username', '').strip()

    if not username:
        return JsonResponse({'is_taken': False, 'suggestion': ''})

    is_taken = User.objects.filter(username__iexact=username).exists()
    suggestion = ''

    if is_taken:
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        suggestion = f"{username}{suffix}"
        while User.objects.filter(username__iexact=suggestion).exists():
            suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
            suggestion = f"{username}{suffix}"

    return JsonResponse({
        'is_taken': is_taken,
        'suggestion': suggestion
    })


def login_user(request):
    if request.method == 'POST':
        identifier = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=identifier, password=password)

        if user is None:
            try:
                u = User.objects.get(email=identifier)
                user = authenticate(request, username=u.username, password=password)
            except User.DoesNotExist:
                user = None

        if user:
            login(request, user)
            return redirect('dashboard')

        messages.error(request, "Invalid credentials")
        return redirect('login')

    return render(request, 'login.html')




def logout_user(request):

    if 'dashboard_user' in request.session:
        del request.session['dashboard_user']

    return redirect("login")


@login_required
def profile_view(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('login')  # fallback safety

    company = Company.objects.filter(email=user.email).first()

    context = {
        'user': user,
        'company': company,
    }
    return render(request, 'profile.html', context)


def verify_pending_user(request, token):
    try:
        pending = PendingUser.objects.get(token=token)
    except PendingUser.DoesNotExist:
        messages.error(request, "Invalid or expired verification link.")
        return redirect('register')

    # generate username now
    username = generate_username(pending.first_name, pending.last_name)

    # Create real user now
    user = User.objects.create_user(
        username=username,
        first_name=pending.first_name,
        last_name=pending.last_name,
        email=pending.email,
        password=None
    )
    user.password = pending.password
    user.is_superuser = False
    user.is_staff = True
    user.is_active = True
    user.save()

    pending.delete()

    messages.success(request, "Your email has been verified successfully!")
    login(request, user)
    return redirect('create-company')

