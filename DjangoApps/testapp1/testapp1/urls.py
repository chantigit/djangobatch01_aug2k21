from django.conf.urls import url
from .views1 import homeview,processview

urlpatterns = [
    url(r'$^',homeview),
    url(r'home/', homeview,name='homel'),
    url(r'process/', processview,name='processl'),
]

