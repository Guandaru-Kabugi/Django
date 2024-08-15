from django.contrib import admin
from .models import Department,Employee
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', )
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('name', )
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','unique_id','email','hire_date')
    list_filter = ('hire_date', )