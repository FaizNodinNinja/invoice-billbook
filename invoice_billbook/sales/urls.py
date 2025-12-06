from django.urls import path
from . import views

urlpatterns = [
    path('overview/', views.sales_overview, name='sales_overview'),
]
