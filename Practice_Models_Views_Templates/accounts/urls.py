from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import SignUpView
from . import views
urlpatterns = [
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/profile/',
             TemplateView.as_view(template_name='account/profile.html'),
             name='profile'),
    path("registration/signup/", SignUpView.as_view(), name="templates/registration/signup"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]