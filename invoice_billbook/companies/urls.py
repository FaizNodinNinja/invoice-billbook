from django.urls import path
from . import views


urlpatterns = [
    path('add-company/', views.add_company, name='add-company'),
    path('company-list/', views.company_list, name='company-list'),
    path('create-company/', views.company_create, name='create-company'),

]
