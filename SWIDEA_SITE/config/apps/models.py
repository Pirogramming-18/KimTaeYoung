from django.db import models
# Create your models here.

class devTool(models.Model):
  name = models.CharField(max_length=20)
  classification = models.CharField(max_length = 20)
  content = models.TextField(null = True)

  def __str__(self):
      return f'{self.name}'




class Idea(models.Model):
  
  
  name = models.CharField(max_length=20)
  image = models.ImageField(blank = True, upload_to="idea/%Y%m%d")
  content = models.TextField(null = True)
  interest_degree = models.IntegerField(default = 0)
  update_at = models.DateTimeField(auto_now=True)
  dev_tool = models.ForeignKey(devTool, on_delete=models.SET_NULL, null=True)

  

class ideaStar(models.Model):
  count = models.BooleanField(default = 0)
  star = models.OneToOneField(Idea, on_delete=models.CASCADE, name = "idea_star")

  
