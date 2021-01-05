from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"hello/table.html")

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})
    
