from django.shortcuts import render , redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm 
from django import forms
from cloudinary.forms import cl_init_js_callbacks
from django.urls import reverse_lazy, reverse



def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #If the form valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')
        else:
            # No, Show Error
            return HttpResponseRedirect("form.erros.as_json()")
    
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form = PostForm()
    # Show
    return render(request, 'posts.html',
                    {'posts': posts})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,  instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm
        return render(request, 'edit.html',{'post':post , 'form':form})


    

def Like(request,post_id):
    post = Post.objects.get(id= post_id)
    new_value=post.likes+1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')

