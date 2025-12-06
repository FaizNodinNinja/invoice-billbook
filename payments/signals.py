from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment

@receiver(post_save, sender=Payment)
def update_invoice_status(sender, instance, **kwargs):
    invoice = instance.invoice
    total_paid = sum(p.amount for p in invoice.payments.all())
    if total_paid >= invoice.total_amount:
        invoice.status = 'paid'
    elif total_paid > 0:
        invoice.status = 'unpaid'  # optionally use 'partial'
    else:
        invoice.status = 'unpaid'
    invoice.save()
