from django.conf.urls import url
from django.contrib import admin
from empdata.views import homev,empregv,empregprocess,showallempv,showoneempformv,searchemp

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'$^',homev),
    url(r'home/', homev,name='homel'),
    url(r'empreg/', empregv,name='empregl'),
    url(r'empregprocess/', empregprocess,name='empregprocessl'),
    url(r'showallemp/',showallempv,name='showallempl'),
    url(r'showemp/',showoneempformv,name='showempl'),
    url(r'searchemp',searchemp,name='searchemp')
]
