from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    registration_number = models.CharField(max_length=50, unique=True, null=False)
    enrollment_date = models.DateField()
class Instructor(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    unique_number = models.CharField(max_length=50, unique=True, null=False)
    employment_date = models.DateField()

class Course(models.Model):
    name = models.CharField(max_length=50)
    instructors = models.ManyToManyField(Instructor,related_name='courses')
    students = models.ManyToManyField(Student,related_name='courses')
    

