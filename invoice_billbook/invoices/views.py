from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import InvoiceForm

from django.contrib import messages
import logging
from django.http import HttpResponse
from django.template import loader

from quotations.models import Quotation, QuotationItem
from clients.models import Client
from companies.models import Company

from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from weasyprint import HTML
from xhtml2pdf import pisa
import io
from django.template.loader import get_template
from django.utils.timezone import now
from .models import Invoice

logger = logging.getLogger(__name__)


# Create your views here.

def generate_invoice(request):
    return render(request, 'invoice_list.html', )


def add_invoice(request):
    if request.method == "POST":
        invoiceform = InvoiceForm(request.POST, request.FILES)
        if invoiceform.is_valid():
            try:
                instance = invoiceform.save(commit=False)
                instance.save()
                messages.success(request, "invoice add sucsess")
                return redirect('add-invoice')
            except ValidationError as e:
                logger.warning(f"Validation error: {e}")
                messages.error(request, "Invalid data error")

            except Exception:
                logger.error(f"Unexpected error in invoice")
                messages.error(request, "something went wrong. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        invoiceform = InvoiceForm
    context = {
        'form': invoiceform
    }
    return render(request, 'add_invoice.html', context)


def invoice_list(request):
    invoicelists = Invoice.objects.all()
    # Debug prints
    template = loader.get_template('invoice_list.html')

    context = {
        'invoicelists': invoicelists,
    }
    return HttpResponse(template.render(context, request))


def edit_invoice(request):
    return render(request, 'edit_invoice.html', )


def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    quotation = invoice.quotation
    items = quotation.items.all() if quotation else []
    return render(request, 'invoice_detail.html', {
        'invoice': invoice,
        'quotation': quotation,
        'items': items,
    })


def generate_invoice_number():
    today = now().strftime("%Y%m%d")  # e.g. 20250918

    # Count how many invoices already created today
    count = Invoice.objects.filter(date=now().date()).count() + 1

    number = f"INV-{today}-{count:03d}"

    # Double-check uniqueness
    while Invoice.objects.filter(invoice_number=number).exists():
        count += 1
        number = f"INV-{today}-{count:03d}"

    return number


# ✅ Ye sirf PDF banata hai aur new tab me open karta hai
from .utils import link_callback


def invoice_pdf(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    quotation = invoice.quotation
    items = quotation.items.all() if quotation else []

    html_string = render(request, "invoice_detail.html", {
        "invoice": invoice,
        "quotation": quotation,
        "items": items,
    }).content.decode("utf-8")

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="invoice_{invoice.invoice_number}.pdf"'

    pisa_status = pisa.CreatePDF(
        io.BytesIO(html_string.encode("utf-8")),
        dest=response,
        encoding="utf-8",
        link_callback=link_callback  # 👈 yaha use karo
    )

    if pisa_status.err:
        return HttpResponse("Error generating PDF")
    return response


# ✅ Ye invoice create karta hai aur fir uske PDF view pe redirect karta hai
def create_invoice(request):
    clients = Client.objects.all()
    company = Company.objects.first()

    if request.method == "POST":
        # Client select / new client
        client_id = request.POST.get("client")
        if client_id and client_id != "new":
            client = Client.objects.get(id=client_id)
        else:
            client = Client.objects.create(
                name=request.POST.get("new_client_name"),
                email=request.POST.get("new_client_email"),
                phone=request.POST.get("new_client_phone"),
                address=request.POST.get("new_client_address"),
                country="India",
            )

        # Quotation create
        quotation = Quotation.objects.create(
            client=client,
            company=company,
            quotation_number=f"QT-{Quotation.objects.count() + 1:03d}",
            date=request.POST.get("date") or now().date(),
            due_date=request.POST.get("due_date") or now().date(),
            terms="Payment within 7 days",
            notes="Thank you for your business!",
            subtotal=request.POST.get("subtotal") or 0,
            tax=float(request.POST.get("tax_rate") or 0),
            total=request.POST.get("total") or 0,
        )

        # Items add
        descriptions = request.POST.getlist("description[]")
        quantities = request.POST.getlist("quantity[]")
        unit_prices = request.POST.getlist("unit_price[]")
        totals = request.POST.getlist("total[]")

        for desc, qty, price, total in zip(descriptions, quantities, unit_prices, totals):
            if desc.strip():
                QuotationItem.objects.create(
                    quotation=quotation,
                    description=desc,
                    quantity=int(qty or 0),
                    unit_price=float(price or 0),
                    total=float(total or 0),
                )

        # Invoice create
        invoice = Invoice.objects.create(
            client=client,  # 👈 yaha add karo
            quotation=quotation,
            invoice_number=generate_invoice_number(),
            date=request.POST.get("date") or now().date(),
            due_date=request.POST.get("due_date") or now().date(),
            total_amount=request.POST.get("total") or 0,
            status="unpaid",
        )

        # ✅ Ab sidha PDF view pe redirect karenge
        # print("DEBUG INVOICE ID:", invoice.pk)

        return redirect("invoice_pdf", pk=invoice.pk)

    return render(request, "create_invoice.html", {"clients": clients})
