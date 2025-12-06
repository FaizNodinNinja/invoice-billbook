from django.shortcuts import render, redirect
from .forms import LeadForm
from .models import Lead
from django.contrib import messages
from .models import (Industry, IndustryType,Country, State, City, ClientStatus)
import logging
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import StateForm, CityForm, IndustryForm, IndustryTypeForm, ClientStatusForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from clients.models import Client
from invoices.models import Invoice

logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    return render(request, 'index.html')

def dashboard(request):

    # 📊 Dashboard data
    total_customers = Client.objects.count()
    total_invoices = Invoice.objects.count()
    # total_payments = Payment.objects.count()
    # total_products = Product.objects.count()

    context = {
        'total_customers': total_customers,
        'total_invoices': total_invoices,
    }

    return render(request, 'dashboard.html', context)


def add_lead(request):
    industrynames = Industry.objects.all()
    industrytypes = IndustryType.objects.all()
    countries = Country.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    statuses = ClientStatus.objects.all()

    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)  # Option to modify before saving
                # instance.created_by = "Anonymous"  # Only if your model supports this
                instance.save()
                messages.success(request, "Lead added successfully!")
                return redirect('add-lead')
            except ValidationError as e:
                logger.warning(f"Validation error: {e}")
                messages.error(request, "Invalid data submitted.")
            except Exception as e:
                logger.error(f"Unexpected error in add_lead: {e}")
                messages.error(request, "Something went wrong. Please try again.")

        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = LeadForm()

    context = {
        'form': form,
        'industry_Name': industrynames,
        'industry_type': industrytypes,
        'countries': countries,
        'states': states,
        'cities': cities,
        'client_statuses': statuses,
    }
    return render(request, 'pages/add_lead.html', context)


def lead_sheet(request):


    search_query = request.GET.get('search', '')
    leads = Lead.objects.select_related(
        'industry', 'industrytype',
        'country', 'state', 'city', 'clientstatus'
    ).all()

    if search_query:
        terms = search_query.strip().split()
        q_objects = Q()

        for term in terms:
            # q_objects |= Q(client_name__icontains=term)
            # q_objects |= Q(phone_no__icontains=term)
            # q_objects |= Q(industry__industry__icontains=term)
            # q_objects |= Q(industrytype__industrytype__icontains=term)
            # q_objects |= Q(country__country__icontains=term)
            # q_objects |= Q(state__state__icontains=term)
            # q_objects |= Q(city__city__icontains=term)
            # q_objects |= Q(clientstatus__clientstatus__icontains=term)

            # 🔥 STARTS WITH matching also added
            q_objects |= Q(client_name__istartswith=term)
            q_objects |= Q(industry__industry__istartswith=term)
            q_objects |= Q(industrytype__industrytype__istartswith=term)
            q_objects |= Q(country__country__istartswith=term)
            q_objects |= Q(state__state__istartswith=term)
            q_objects |= Q(city__city__istartswith=term)
            q_objects |= Q(clientstatus__clientstatus__istartswith=term)

        leads = leads.filter(q_objects)

    return render(request, 'pages/lead_sheet.html', {'leads': leads})


def edit_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)

    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "Lead updated successfully!")
            return redirect('lead-sheet')
    else:
        form = LeadForm(instance=lead)

    context = {
        'form': form,
        'lead': lead,
        'industry_Name': Industry.objects.all(),
        'industry_type': IndustryType.objects.all(),
        'countries': Country.objects.all(),
        'states': State.objects.all(),
        'cities': City.objects.all(),
        'client_statuses': ClientStatus.objects.all(),
    }
    return render(request, 'pages/add_lead.html', context)


def delete_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)

    if request.method == 'POST':
        lead.delete()

        # अगर request AJAX है तो JSON में response भेजेंगे
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"success": True, "message": "Lead deleted successfully!", "id": pk})

        messages.success(request, "Lead deleted successfully!")
        return redirect('lead-sheet')

    return redirect('pages/lead-sheet')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


@csrf_exempt
def add_industry_ajax(request):
    if request.method == "POST":
        industry_name = request.POST.get('industry')
        if industry_name:
            industry, created = Industry.objects.get_or_create(industry=industry_name)
            return JsonResponse({'id': industry.id, 'name': industry.industry})
        else:
            return JsonResponse({'error': 'Industry name is required'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def add_industrytype_ajax(request):
    if request.method == "POST":
        industrytype_name = request.POST.get('industrytype')
        if industrytype_name:
            industrytype, created = IndustryType.objects.get_or_create(industrytype=industrytype_name)
            return JsonResponse({'id': industrytype.id, 'name': industrytype.industrytype})
        else:
            return JsonResponse({'error': 'industrytype name is required'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def add_country_ajax(request):
    if request.method == "POST":
        country_name = request.POST.get('country')
        if country_name:
            country, created = Country.objects.get_or_create(country=country_name)
            return JsonResponse({'id': country.id, 'name': country.country})
        else:
            return JsonResponse({'error': 'country name is required'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def add_state_ajax(request):
    if request.method == "POST":
        state_name = request.POST.get('state')
        if state_name:
            state, created = State.objects.get_or_create(state=state_name)
            return JsonResponse({'id': state.id, 'name': state.state})
        else:
            return JsonResponse({'error': 'state name is required'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def add_city_ajax(request):
    if request.method == "POST":
        city_name = request.POST.get('city')
        if city_name:
            city, created = City.objects.get_or_create(city=city_name)
            return JsonResponse({'id': city.id, 'name': city.city})
        else:
            return JsonResponse({'error': 'city name is required'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)





@csrf_exempt
def add_clientstatus_ajax(request):
    if request.method == "POST":
        clientstatus_name = request.POST.get('clientstatus')
        if clientstatus_name:
            clientstatus, created = ClientStatus.objects.get_or_create(clientstatus=clientstatus_name)
            return JsonResponse({'id': clientstatus.id, 'name': clientstatus.clientstatus})
        else:
            return JsonResponse({'error': 'clientstatus name is required'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


