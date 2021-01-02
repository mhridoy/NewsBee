from django.contrib import admin
from .models import Post,UserCountry
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
@admin.register(UserCountry)
class UserCountryAdmin(admin.ModelAdmin):
    pass