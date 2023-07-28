from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('courses_detail/<int:post_id>/', views.courses_detail, name='courses_detail'),
]