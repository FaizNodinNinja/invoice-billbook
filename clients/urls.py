from django.urls import path
from . import views

urlpatterns = [
    path('add-customer/', views.add_customer, name='add-customer'),
    path('edit-customer/', views.edit_customer, name='edit-customer'),
    path('delete-customer/', views.delete_customer, name='delete-customer'),
    path('customers/', views.customer_list, name='customer-list'),
]
