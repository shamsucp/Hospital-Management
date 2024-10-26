# hospital/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def booking(request):
    return render(request,"booking.html")
def docters(request):
    return render(request,"docters.html")
def contuct(request):
    return render(request,"conduct.html")
def department(request):
    return render(request,"department.html")


