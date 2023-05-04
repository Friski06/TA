
from django.contrib import admin
from django.urls import path, include
from dataabsen import views as DataAbsen
from datapegawai import views as Datapegawai
from cutiizin import views as Cutiizin
from spt import views as Spt
from penilaian import views as Penilaian

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('datapegawai/',Datapegawai.datapegawai, name='datapegawai'),
    path('dataabsen/', DataAbsen.dataabsen, name='dataabsen'),
    path('cutiizin/',Cutiizin.cutiizin, name='cutiizin'),
    path('spt/',Spt.spt, name='spt'),
     path('penilaian/',Penilaian.penilaian, name='penilaian'),
    path('login/',include('login.urls')),
]
