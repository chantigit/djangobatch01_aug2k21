
from django.contrib import admin
from django.urls import path, include
from app1 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student', views.StudentViewSet, basename='student')
router.register('course', views.CourseViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]