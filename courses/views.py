from .models import Course
from django.shortcuts import render

def courses(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})

def courses_detail(request):
    return render(request, "courses_detail.html")
