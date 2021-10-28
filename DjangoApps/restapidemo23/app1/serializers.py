from .models import Student,Course
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
 class Meta:
  model = Course
  fields = ['id', 'name', 'fee', 'courseStartingDate']

class StudentSerializer(serializers.ModelSerializer):
 course = CourseSerializer(read_only=True)
 class Meta:
  model = Student
  fields = ['id', 'rollNumber','name', 'course','age']
 def validate(self, data):
  age = data.get('age')
  if age < 20:
   raise serializers.ValidationError('Age must be above 20')
  return data