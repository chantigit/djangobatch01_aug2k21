from django.contrib import admin
from .models import Student,Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
 list_display = ['id', 'rollNumber','name', 'course','age']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'fee', 'courseStartingDate']