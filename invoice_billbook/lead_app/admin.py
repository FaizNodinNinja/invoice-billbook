from django.contrib import admin

# Register your models here.

from .models import Lead, IndustryType, Country, State, City, ClientStatus, Industry

# Basic registration - simplest approach
admin.site.register(Lead)
admin.site.register(Industry)
admin.site.register(IndustryType)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(ClientStatus)
