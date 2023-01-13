from django.db import models

# Create your models here.

class Post(models.Model):

  genre_list = (
    ("액션", "액션"),
    ("SF", "SF"),
    ("로맨스", "로맨스"),
    ("코미디", "코미디"),
    ("느와르", "느와르"),
    ("공포", "공포"),
    ("스릴러", "스릴러"),
  )

  title = models.CharField(max_length = 50)
  released_year = models.IntegerField(null=True, default = 0)
  genre = models.CharField(blank = True, max_length=10, choices=genre_list)
  star_rating = models.FloatField()
  review = models.TextField()
  director = models.CharField(max_length = 30)
  actor = models.TextField(null=True)
  time = models.IntegerField(null=True, default = 0)


  