from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def main (request): 
  posts = Post.objects.all()
  
  ctx = {"posts" : posts}
  return render(request, "post_list.html", ctx)

def post_create(request):

  if request.method == "POST":
    form = PostForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect("/")
  
  form = PostForm()

  ctx = {"form" : form}

  return render(request, "post_create.html", ctx)

def post_read(request, pk):

  post = Post.objects.get(id=pk)
  comments = Comment.objects.filter(post_comment = pk)

  ctx = {"post" : post, "comments" : comments}

  return render(request, "post_read.html", ctx)



# html상에서 불러온 걸 실시간으로 처리
# 해당 포스트의 외래키를 가진 댓글 객체를 생성해서 저장  
@csrf_exempt
def comment_create(request):
  body_unicode = request.body.decode('utf-8')
  
  req = json.loads(body_unicode) # request.body => {id : 1, type : 'like'}
  post_id = req['id'] 
  content = req['content']
  
  post = Post.objects.get(id = post_id)

  comment = Comment.objects.create(post_comment = post,
  content = content)
  comment.save()
  return JsonResponse({'post_id' : post_id, 'comment_id' : comment.pk, 'content' : content, 'status' : 1})
  
@csrf_exempt
def comment_delete(request):
  body_unicode = request.body.decode('utf-8')

  req = json.loads(body_unicode)

  comment_id = req['id']
  
  comment = Comment.objects.get(id = comment_id)
  print(comment_id, comment.pk)

  comment.delete()
  return JsonResponse({'post_id' : None, 'comment_id' : comment_id, 'content' : "", 'status' : 0})

@csrf_exempt
def change_like(request):
  body_unicode = request.body.decode('utf-8')

  req = json.loads(body_unicode)

  status = req['status']
  post_id = req['id']

  status = not status
  post = Post.objects.get(id = post_id)
  post.like = status
  post.save()

  return JsonResponse({'status' : status, 'id' : post_id})
