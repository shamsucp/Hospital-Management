# hospital/urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name='home'),
        path('about/',views.about,name='about'),
        path('booking/',views.booking,name='booking'),
        path('docters/',views.docters,name='docters'),
        path('contuct/',views.contuct,name='contuct'),
        path('department/',views.department,name='department'),
]
