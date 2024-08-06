from django.db import models

# Create your models here.
class Student(models.Model):
    registration_number = models.CharField(max_length=200, unique=True)
    student_name = models.CharField(max_length=200)
    student_age = models.IntegerField()
    student_email = models.EmailField(max_length=200,unique=True)
    student_courses = models.CharField(max_length=200)
    enrolled_date = models.DateField()
    def __str__(self):
        return f"Registration Number: {self.registration_number} Student Name: {self.student_name} Student Age: {self.student_age} Student Email: {self.student_email} Student Courses: {list(self.student_courses.split(','))} Enrollment Date: {self.enrolled_date}"
class Instructor(models.Model):
    registration_number = models.CharField(max_length=200, unique=True)
    instructor_name = models.CharField(max_length=200)
    instructor_age = models.IntegerField()
    instructor_email = models.EmailField(max_length=200,unique=True)
    instructor_courses = models.CharField(max_length=200)
    employment_date = models.DateField()
    def __str__(self):
        return f"Registration Number: {self.registration_number} Instructor Name: {self.instructor_name} Instructor Age: {self.instructor_age} Instructor Email: {self.instructor_email} Instructor Courses: {list(self.instructor_courses.split(','))} Employment Date: {self.employment_date}"
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_instructor = models.CharField(max_length=150)
    def __str__(self):
        return f"Course Name: {self.course_name} Instructor Name: {self.course_instructor}"