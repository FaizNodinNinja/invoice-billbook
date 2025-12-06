from django.contrib.messages.context_processors import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import QuotationForm, QuotationItemForm
from .models import Quotation, QuotationItem
import logging
from django.http import HttpResponse
from django.template import loader

logger = logging.getLogger(__name__)


# Create your views here.

def add_quotation(request):
    if request.method == 'POST':
        quotationform = QuotationForm(request.POST, request.FILES)
        if quotationform.is_valid():
            try:
                instance = quotationform.save(commit=False)
                instance.save()
                messages.success(request,'Quotation  added successfully!"')
                return redirect('add-quotation')
            except ValidationError as e:
                logger.warning(f"Validation error: {e}")
                message.error(request, "Invalid data error")
            except Exception as e:
                logger.error(f"Unexpected error in Quotation: {e}")
                messages.error(request, "something went wrong. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        quotationform = QuotationForm
    context = {
        'form': quotationform
    }
    return render(request, 'add_quotation.html', context)


def quotation_list(request):
    quotationlists = Quotation.objects.all()
    # Debug prints
    template = loader.get_template('quotation_list.html')
    context = {
        'quotationlists': quotationlists,
    }
    return HttpResponse(template.render(context, request))


def edit_quotation(request):
    return render(request, 'add_quotation_item.html', )


# ###
def add_quotation_item(request):
    if request.method == 'POST':
        quotationitemform = QuotationItemForm(request.POST, request.FILES)
        if quotationitemform.is_valid():
            try:
                instance = quotationitemform.save(commit=False)
                instance.save()
                messages.success(request, 'Quotation added successfully!"')
                return redirect('add-quotation-item')
            except ValidationError as e:
                logger.warning(f"Validation error: {e}")
                message.error(request, "Invalid data error")
            except Exception as e:
                logger.error(f"Unexpected error in company business: {e}")
                messages.error(requestm, "something went wrong. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        quotationform = QuotationItemForm
    context = {
        'form': quotationform
    }
    return render(request, 'add_quotation_item.html', context)


# ###
def quotation_item_list(request):
    quotationitems = QuotationItem.objects.all()
    template = loader.get_template('quotation_item_list.html')
    context = {
        'quotationitems': quotationitems,
    }
    return HttpResponse(template.render(context, request))


# ###
def edit_quotation_item(request):
    return render(request, 'edit_quotation_item.html', )
