from django.contrib import admin
from .models import Student,Instructor,Course
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','registration_number','enrollment_date')
    list_filter = ('enrollment_date', )
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','unique_number','employment_date')
    list_filter = ('employment_date', )
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )