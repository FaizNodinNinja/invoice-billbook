from django.urls import path
from . import views


urlpatterns = [
    path('add-quotation/', views.add_quotation, name='add-quotation'),
    path('add-quotation-item/', views.add_quotation_item, name='add-quotation-item'),

    path('quotation-list/', views.quotation_list, name='quotation-list'),
    path('quotation-item-list/', views.quotation_item_list, name='quotation-item-list'),
]
