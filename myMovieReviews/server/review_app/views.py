from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django import template
# Create your views here.


def movie_list(request):
  post = Post.objects.all() 
  hours = []
  minutes = []
  for i in post:
    hours.append(i.time//60)
    minutes.append(i.time%60)
  return render(request, "review/movie_list.html", {"outlines" : post, "hours" : hours, "minutes": minutes})

def post_create(request):
  
  if request.method == "POST":
    post = PostForm(request.POST)
    post.save()

    return redirect("/")
  else:
    post = PostForm()
  return render(request, "review/post_create.html", {"post" : post})

def post_read(request, pk):

  post = Post.objects.all().get(id=pk)
  hour = post.time//60
  minute = post.time%60
  return render(request, "review/post_read.html", {"post": post, "hour": hour, "minute": minute})

def post_delete(request, pk):
  if request.method == "POST":
    post = Post.objects.get(id=pk)
    post.delete()
  return redirect("/")

def post_edit(request, pk):
  post = Post.objects.get(id=pk)
  form = PostForm(instance=post)
  if request.method == "POST":
    form = PostForm(request.POST, instance=post)
    form.save()
    return redirect(f"/review/{post.id}")
  return render(request, "review/post_edit.html", {"post" : post, "form": form})