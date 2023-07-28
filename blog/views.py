from django.shortcuts import render, get_object_or_404
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .models import BlogPost

def blogpost(request):
    blogposts = BlogPost.objects.order_by('-published_date')[:10]
    context = {
        'blogposts': blogposts,
        'abbreviated': True,  # indicate that posts should be abbreviated by default
    }
    return render(request, 'blog.html', context)

def post_detail(request, slug):
    blogpost = get_object_or_404(BlogPost, slug=slug)
    context = {
        'blogpost': blogpost,
        'abbreviated': False,  # indicate that post should be displayed in full
    }
    return render(request, 'post_detail.html', context)


def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(generate_slug, sender=blogpost)