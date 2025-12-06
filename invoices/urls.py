from django.urls import path
from . import views


urlpatterns = [

    path('add-invoice/', views.add_invoice, name='add-invoice'),
    path('edit-invoice/', views.edit_invoice, name='edit-invoice'),
    path('invoice-list/', views.invoice_list, name='invoice-list'),

    #generayte invoice
    path("create/", views.create_invoice, name="create-invoice"),

    path('<int:pk>/', views.invoice_detail, name='invoice-detail'),
    path('<int:pk>/pdf/', views.invoice_pdf, name='invoice_pdf'),
]
