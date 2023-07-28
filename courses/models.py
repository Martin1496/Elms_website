from django.db import models
#
# # Create your models here.
class Course(models.Model):
    img: models.ImageField(upload_to='static')
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

class courses(models.Model):
    img: models.ImageField(upload_to='static')
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)



