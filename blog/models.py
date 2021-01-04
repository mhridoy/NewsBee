from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    #photo = models.ImageField(upload_to='news')
class Home(models.Model):
    title = models.TextField(max_length=50, blank = True, null = True)
    category = models.TextField(max_length=50, blank = True, null = True)
    desc = models.TextField(max_length=4000, blank = True, null = True)
    country = models.TextField(max_length=20, blank = True, null = True)
    url = models.URLField(max_length=200, blank = True, null = True)
    
    image_url = models.URLField(max_length = 200,blank= True,null=True)

   

class UserCountry(models.Model):
    country = models.CharField(max_length=100)
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    

class SaveCountry(models.Model):
        s_count = models.TextField(max_length=2,unique=True) 