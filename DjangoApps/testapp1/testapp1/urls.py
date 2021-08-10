from django.conf.urls import url
from .views1 import homepageview,aboutpageview

urlpatterns = [
    url(r'$^',homepageview),
    url(r'home', homepageview),
    url(r'start', homepageview),
    url(r'about', aboutpageview),
]

'''
http://localhost:8000/          => HOME PAGE REQUEST
http://localhost:8000/home      => HOME PAGE REQUEST
http://localhost:8000/start     => HOME PAGE REQUEST
http://localhost:8000/about     => ABOUT PAGE REQUEST
'''