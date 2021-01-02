from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    #photo = models.ImageField(upload_to='news')
class Home(models.Model):
    title = models.CharField(max_length=50, blank = True, null = True)
    category = models.CharField(max_length=10, blank = True, null = True)
    desc = models.CharField(max_length=4000, blank = True, null = True)
    country = models.CharField(max_length=20, blank = True, null = True)
    slug = models.SlugField(default = 'test')
    image_url = models.CharField( max_length=50, blank = True, null = True)

    def __str__(self):
        return self.name

class UserCountry(models.Model):
    country = models.CharField(max_length=100)
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    

