from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('verify/<uidb64>/<token>/', views.verify_email, name='verify_email'),

    path('check-username/', views.check_username, name='check_username'),

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('profile/', views.profile_view, name='profile'),
    path('verify/<str:token>/', views.verify_pending_user, name='verify-pending-user'),

]
