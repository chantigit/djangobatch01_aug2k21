
from django.shortcuts import render

def homeview(request):
    return render(request,'index.html')
def processview(request):
    return render(request, 'process.html')