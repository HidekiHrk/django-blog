from website.models import Post
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
# Create your views here.

def home(request: HttpRequest):
    objs = Post.objects.all()
    return render(request, 'home.html', { 'posts': objs })


def post(request: HttpRequest, slug: str):
    try:
        obj: Post = Post.objects.get(slug=slug)
        return render(request, 'post.html', { 'post': obj })
    except:
        return JsonResponse({'error': 'This post does not exists :C'})
    