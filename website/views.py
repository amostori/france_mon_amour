from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage = request.user
            form.save()
        return redirect('index')
    else: # GET
        posts = Post.objects.filter(manage=request.user)
    return render(request, 'index.html', {'posts': posts})

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'edit_post.html', {'post': post})

@login_required
def delete_post(request, post_id):
    Post.objects.get(pk=post_id).delete()
    return redirect('index')

def example(request):
    return render(request, 'example.html')
