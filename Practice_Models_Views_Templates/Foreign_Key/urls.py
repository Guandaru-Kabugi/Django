from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import SignUpView
from . import views
urlpatterns = [
    # path('', views.employee_list, name='employee_list'),
    # path('employee_json/', views.employee_json, name='employee_list'),
    path('', views.home, name='homepage'),
    path('employee/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/profile/',
             TemplateView.as_view(template_name='account/profile.html'),
             name='profile'),
    path("signup/", SignUpView.as_view(), name="templates/registration/signup"),
    path('logout/', LogoutView.as_view(), name='logout'),

]