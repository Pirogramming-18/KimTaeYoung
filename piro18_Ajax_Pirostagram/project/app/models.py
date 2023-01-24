from django.db import models


class Post(models.Model):
  title = models.CharField(max_length = 30)
  content = models.TextField()
  like = models.BooleanField(default = 0)


class Comment(models.Model):
  post_id = models.ForeignKey(Post, on_delete = models.CASCADE, name = "post_comment")
  content = models.CharField(max_length = 250)


  def __str__ (self):
    return self.content