from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('index')
    else: # GET
        posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'edit_post.html', {'post': post})

def delete_post(request, post_id):
    Post.objects.get(pk=post_id).delete()
    return redirect('index')

def example(request):
    return render(request, 'example.html')