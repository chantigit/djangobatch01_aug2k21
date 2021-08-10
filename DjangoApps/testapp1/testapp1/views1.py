
from django.http import HttpResponse
#view1
def homepageview(request):
    return HttpResponse('<h1>Welcome to Home Page</h1>')
#view2
def aboutpageview(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')