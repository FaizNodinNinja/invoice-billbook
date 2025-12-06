from django.contrib import admin

# Register your models here.

from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount', 'method', 'payment_date', 'reference_number')
    list_filter = ('method', 'payment_date')
    search_fields = ('invoice__invoice_number', 'reference_number')
