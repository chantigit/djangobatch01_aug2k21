from django.shortcuts import render


def home(request):
    myid=101
    myname='Ajay'
    myage=26
    my_dict={'pid':myid,'pname':myname,'page':myage}
    return render(request,'index.html',my_dict)