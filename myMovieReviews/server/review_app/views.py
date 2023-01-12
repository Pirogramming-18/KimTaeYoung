from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def movie_list(request):
  post = Post.objects.all()

  return render(request, "review/movie_list.html", {"outlines" : post})

def post_create(request):
  if request.method == "POST":
    Post.objects.create(
      title = request.POST["title"],
      released_year = request.POST["released_year"],
      star_rating = request.POST["star_rating"],
      review = request.POST["review"],
      director = request.POST["director"],
      actor = request.POST["actor"]
    )
    return redirect("/")
  return render(request, "review/post_create.html")

def post_read(request, pk):

  post = Post.objects.all().get(id=pk)
  return render(request, "review/post_read.html", {"post": post})

def post_delete(request, pk):
  if request.method == "POST":
    post = Post.objects.get(id=pk)
    post.delete()
  return redirect("/")

def post_edit(request, pk):
  post = Post.objects.get(id=pk)

  if request.method == "POST":
    post.title = request.POST["title"]
    post.released_year = request.POST["released_year"]
    post.star_rating = request.POST["star_rating"]
    post.review = request.POST["review"]
    post.director = request.POST["director"]
    post.actor = request.POST["actor"]
    post.save()
    return redirect(f"/review/{post.id}")
  return render(request, "review/post_edit.html", {"post" : post})