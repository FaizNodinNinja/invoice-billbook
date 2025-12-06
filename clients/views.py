from django.shortcuts import render
from .models import Client
from .forms import ClientFrom
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib import messages
import logging
# from django.shortcuts import get_object_or_404
# from django.db.models import Q
from django.http import HttpResponse
from django.template import loader


# Create your views here.
logger = logging.getLogger(__name__)

def add_customer(request):

    if request.method == 'POST':
        clientform = ClientFrom(request.POST)
        if clientform.is_valid():
            try:
                instance = clientform.save(commit=False)
                instance.save()
                messages.success(request, "Customer added successfully!")
                return redirect('add-customer')
            except ValidationError as e:
                logger.warning(f"Validation error: {e}")
                messages.error(request, "Invalid data submitted.")
            except Exception as e:
                logger.error(f"Unexpected error in add_customer: {e}")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        clientform = ClientFrom()

    context = {
        'form': clientform,
    }
    return render(request, 'add_customer.html', context)


def customer_list(request):
    clients = Client.objects.all()
    total_customers = clients.count()
    template = loader.get_template('customer_list.html')
    context = {
        'clients': clients,
        'total_customers': total_customers
    }
    return HttpResponse(template.render(context, request))



def edit_customer(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        clientform = ClientFrom(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Lead updated successfully!")
            return redirect('customer_list')
    else:
        clientform = ClientFrom(instance=client)

    context = {
        'clientform': clientform,
        'client': client,

    }
    return render(request, 'add_customer.html', context)


def delete_customer(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        client.delete()
        messages.success(request, "customer deleted successfully!")
        return redirect('customer_list')
    # If method is not POST, redirect anyway (prevent error)
    return redirect('customer_list')

#
# def customet_list(request):
#     pass
#
# def edit_customer(request):
#     pass
#
# def delete_customer(request):
#     pass