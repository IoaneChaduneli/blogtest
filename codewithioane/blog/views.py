from django.shortcuts import render
from blog.models import BlogPost
# Create your views here.

def Blog_view_list(request):
    context = {}
    blog_posts = BlogPost.objects.all()
    context['blog_posts'] = blog_posts
    return render(request, 'base.html', context)
