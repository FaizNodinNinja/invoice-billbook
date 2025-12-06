from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),
                  path('dashboard/', views.dashboard, name='dashboard'),
                  path('add-lead/', views.add_lead, name='add-lead'),
                  path('lead-sheet/', views.lead_sheet, name='lead-sheet'),
                  path('edit-lead/<int:pk>/', views.edit_lead, name='edit-lead'),
                  path('delete-lead/<int:pk>/', views.delete_lead, name='delete-lead'),

                  path('ajax/add-industry/', views.add_industry_ajax, name='add_industry_ajax'),
                  path('ajax/add-industrytype/', views.add_industrytype_ajax, name='add_industrytype_ajax'),
                  path('ajax/add-country/', views.add_country_ajax, name='add_country_ajax'),
                  path('ajax/add-state/', views.add_state_ajax, name='add_state_ajax'),
                  path('ajax/add-city/', views.add_city_ajax, name='add_city_ajax'),
                  path('ajax/add-clientstatus/', views.add_clientstatus_ajax, name='add_clientstatus_ajax'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
