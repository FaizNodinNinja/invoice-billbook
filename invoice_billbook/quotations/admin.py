from django.contrib import admin
from .models import Quotation, QuotationItem


# Register your models here.

admin.site.register(Quotation)
admin.site.register(QuotationItem)
