from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def Home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

