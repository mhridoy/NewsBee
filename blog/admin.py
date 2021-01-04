from django.contrib import admin
from .models import Post,UserCountry,Home,SaveCountry
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
@admin.register(UserCountry)
class UserCountryAdmin(admin.ModelAdmin):
    list_display = ['id','country','user']

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title','category','desc',
    'country','url','image_url'
    ]
@admin.register(SaveCountry)
class SaveCountry(admin.ModelAdmin):
    list_display = ['s_count']


