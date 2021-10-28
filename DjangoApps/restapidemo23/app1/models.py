from django.db import models

class Course(models.Model):
 name = models.CharField(max_length=100)
 fee = models.IntegerField()
 courseStartingDate=models.DateField()

 def __str__(self):
  return self.name

class Student(models.Model):
 rollNumber=models.CharField(max_length=100)
 name = models.CharField(max_length=100)
 course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
 age = models.IntegerField()

 def __str__(self):
  return self.name