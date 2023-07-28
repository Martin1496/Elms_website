from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)

