from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255 , verbose_name="Company Name")
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    currency = models.CharField(max_length=10, default="INR")
    gst_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name