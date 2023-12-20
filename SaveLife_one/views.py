from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from django.http import JsonResponse
from .forms import BlogForm
from .models import Blog,Comment



# Create your views here.

# Home view

def Home(request):
    return render (request, 'Home/index.html')



# About view

def About(request):
    return render (request, 'About/about.html')



# Blog view

class List(ListView):
    template_name='Blog/index.html'
    queryset = Blog.objects.all()
    paginate_by=3
    
# Vue pour incrémenter le nombre de partages
def increment_shares(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    post.shares += 1
    post.save()
    return JsonResponse({'shares': post.shares})

    
def detailView(request,slug):
    post = Blog.objects.get(slug=slug)
    comments = post.comments.all()
    if request.method == "POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.post=post
            form.save()
            return redirect('detail',slug=post.slug)
    else:
        form = BlogForm()
    content = {
        'article':post,
        'comments':comments,
        'form':form
    }
    
    return render(request,'Blog/update.html',content)
