"""
URL configuration for lead project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('admin/logout/', auth_views.LogoutView.as_view(next_page='/admin/login/')),
    path('admin/', admin.site.urls),
    path('', include("lead_app.urls")),

    path('accounts/', include('accounts.urls')),
    path('clients/', include('clients.urls')),
    path('companies/', include('companies.urls')),
    path('quotations/', include('quotations.urls')),
    path('invoices/', include('invoices.urls')),
    path('notifications/', include('notifications.urls')),
    path('products/', include('products.urls')),
    path('expenses/', include('expenses.urls')),
    path('payments/', include('payments.urls')),
    path('sales/', include('sales.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
