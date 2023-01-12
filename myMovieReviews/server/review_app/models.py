from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length = 50)
  released_year = models.IntegerField(null=True, default = 0)
  genre = models.TextField(null=True)
  star_rating = models.FloatField()
  review = models.TextField()
  director = models.CharField(max_length = 30)
  actor = models.TextField(null=True)

