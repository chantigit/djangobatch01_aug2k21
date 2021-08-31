from django.shortcuts import render

# Create your views here.
from app1.forms import Form1,Form2,Form3


def one_v(request):
    form1=Form1()
    return render(request,'one.html',{'form':form1})
def two_v(request):
    #Get name from html from
    name=request.GET.get('name')
    #Set name into session
    request.session['key1']=name
    form1 = Form2()
    return render(request,'two.html',{'form':form1})
def three_v(request):
    # Get city from html from
    city = request.GET.get('city')
    # Set city into session
    request.session['key2'] = city
    form1 = Form3()
    return render(request,'three.html',{'form':form1})
def final_v(request):
    # Get age from html from
    age = request.GET.get('age')
    # Set age into session
    request.session['key3'] = age
    # Get all session data & display into final.html
    return render(request,'final.html')