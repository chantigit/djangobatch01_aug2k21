from .serializers import StudentSerializer,CourseSerializer
from rest_framework import viewsets
from .models import Student,Course

class StudentViewSet(viewsets.ModelViewSet):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
 queryset = Course.objects.all()
 serializer_class = CourseSerializer
