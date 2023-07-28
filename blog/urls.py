from django.urls import path
from .views import post_detail
from . import views

urlpatterns = [
    path('', views.blogpost, name='Blogpost'),
    path('blog/post_detail/<slug:slug>/', post_detail, name='post_detail'),
]

