from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    manager = models.OneToOneField('Employee', on_delete=models.PROTECT, null=True, blank=True)
# class Company(models.Model):
#     name = models.CharField(max_length=100)
#     default_department = models.ForeignKey(Department, on_delete=models.SET_DEFAULT, default=1)
class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    unique_id = models.CharField(max_length=15, null=False,unique=True)
    email = models.EmailField()
    hire_date = models.DateField()
    employee_department = models.ForeignKey(Department, on_delete=models.CASCADE, default=6, related_name='employees')
    # employee_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    def __str__(self) -> str:
        return f"First Name: {self.first_name} Last Name: {self.last_name}"
    