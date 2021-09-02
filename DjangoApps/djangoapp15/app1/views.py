from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


def sayHi1(request):
    return HttpResponse('<h1>Hi from FBV using HttpResponse</h1>')
def sayHi2(request):
    x='Hi from FBV using render'
    return render(request,'one.html',{'msg':x})
class Hello1(View):
    def get(self,request):
        return HttpResponse('<h1>Hello from CBV using HttpResponse</h1>')
class Hello2(TemplateView):
    template_name = 'two.html'