
from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.main, name = "main"),
  path('comment_create', views.comment_create, name = "comment_create"),
  path('comment_delete', views.comment_delete, name = "comment_delete"),
  path('read/<int:pk>', views.post_read, name = "post_read"),
  path('create', views.post_create, name = "post_create"),
  path('change_like', views.change_like, name = "change_like"),
]