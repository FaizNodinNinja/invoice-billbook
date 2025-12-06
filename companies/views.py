from django.shortcuts import render, redirect,HttpResponse
from .models import Company
from .forms import CompanyBusiness

from django.core.exceptions import ValidationError
from django.contrib import messages
import logging
from django.http import HttpResponse
from django.template import loader
# from django.shortcuts import get_object_or_404
# from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
logger = logging.getLogger(__name__)

# Create your views here.

# companies/views.py
@login_required
def company_create(request):
    if request.method == "POST":
        form = CompanyBusiness(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.email = request.user.email   # 🔴 yahan auto set ho jayega
            company.save()
            messages.success(request, "Company profile created successfully!")
            return redirect("home")
    else:
        form = CompanyBusiness()

    return render(request, "company_form.html", {
        "form": form,
        "user_email": request.user.email,
        "user_fullname": f"{request.user.first_name} {request.user.last_name}".strip(),
    })


def add_company(request):
    if request.method == 'POST':
        companyform = CompanyBusiness(request.POST, request.FILES)  # Add request.FILES for logo uploads
        if companyform.is_valid():
            try:
                instance = companyform.save(commit=False)
                instance.save()
                messages.success(request, "Company business added successfully!")
                return redirect('add-company')
            except ValidationError as e:
                logger.warning(f"Validation error: {e}")
                messages.error(request, "Invalid data submitted.")
            except Exception as e:
                logger.error(f"Unexpected error in company business: {e}")
                messages.error(request, "Something went wrong. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        companyform = CompanyBusiness()

    context = {
        'form': companyform,  # Sending as 'form' to match template
    }
    return render(request, 'add_company.html', context)


def company_list(request):
    companys = Company.objects.all()

    # Debug prints

    template = loader.get_template('company_list.html')
    context = {
        'companys': companys,
    }
    return HttpResponse(template.render(context, request))

