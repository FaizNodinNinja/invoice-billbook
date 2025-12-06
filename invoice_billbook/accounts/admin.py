from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import PendingUser

# Unregister the default User admin
admin.site.unregister(User)


admin.site.register(PendingUser)

# Create a new User admin
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'is_superuser', 'is_staff', 'is_active',  'date_joined', 'last_login'
    )
    list_filter = ('is_superuser','is_staff', 'is_active',   'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('date_joined',)