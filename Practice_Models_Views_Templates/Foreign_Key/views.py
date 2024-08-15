from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Department,Employee
from django.views.generic import TemplateView,DetailView,UpdateView, CreateView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
def home (request):
    return render(request,'Foreign_Key/home.html', {})
# def employee_list (request):
#     employees = Employee.objects.all()
#     context = {'employee_list': employees}
#     return render(request,'Foreign_Key/index.html',context)
def employee_json (request):
    # Query all employees
    employees = Employee.objects.all()
    
    # Create a list of dictionaries with employee data
    employee_data = []
    for employee in employees:
        employee_data.append({
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'email': employee.email,
            'unique_id': employee.unique_id,
            'hire_date': employee.hire_date.strftime('%Y-%m-%d'),  # Convert date to string
        })
    
    # Return the list as JSON
    return JsonResponse(employee_data, safe=False)


# class HelloView(TemplateView):
#     template_name = 'Foreign_Key/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         # Query all employees
#         employees = Employee.objects.all()
        
#         # Create a list of dictionaries with employee data
#         employee_data = []
#         for employee in employees:
#             employee_data.append({
#                 'first_name': employee.first_name,
#                 'last_name': employee.last_name,
#                 'email': employee.email,
#                 'unique_id': employee.unique_id,
#                 'hire_date': employee.hire_date.strftime('%Y-%m-%d'),  # Convert date to string
#             })
        
#         # Add employee_data to the context
#         context['employee_data'] = employee_data
#         return context
class HelloView(View):
    def get(self, request, *args, **kwargs):
        # Query all employees
        employees = Employee.objects.all()

        # Create a list of dictionaries with employee data
        employee_data = []
        for employee in employees:
            employee_data.append({
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'email': employee.email,
                'unique_id': employee.unique_id,
                'hire_date': employee.hire_date.strftime('%Y-%m-%d'),  # Convert date to string
            })
        
        # Return the data as JSON
        return JsonResponse(employee_data, safe=False)

class EmployeeUpdateView(UpdateView):
    
    """A class-based view for updating details of a specific book."""
    model = Employee
    fields = ['first_name', 'last_name', 'unique_id','email','hire_date']  # Specify fields to be editable
    template_name = 'Foreign_Key/employee_update_form.html'
    success_url = reverse_lazy('employee_list')  # URL to redirect after successful update

    def form_valid(self, form):
        """Executes custom logic after form validation."""
        response = super().form_valid(form)  # Call default form validation
        print("Form is valid, redirecting...")
        # Perform additional actions after successful update (e.g., send notifications)
        return response



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"