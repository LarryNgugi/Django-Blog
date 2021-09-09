from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)
    views = models.IntegerField(default = 0,blank=True)
    slug = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    tittle = models.CharField(max_length= 100)
    message = models.TextField()
    likes = models.IntegerField(default=0,blank=True)
    dislikes = models.IntegerField(default=0,blank=True)
    slug = models.SlugField(max_length=200)
    image_url = models.ImageField()
    views = models.IntegerField(default=0,blank=True)
    keywords = models.TextField()
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Post'
    

class Comment (models.Model):
    message = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=False)
    Post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=False,null=False)
    likes = models.IntegerField(default=0,blank=True)
    dislikes = models.IntegerField(default=0,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Comment'

class Feedback (models.Model):
    message = models.TextField()
    name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    phone_number = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Feedback'

class Seo(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.TextField()
    occassion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    class Meta:
        verbose_name_plural = 'SEO'





    
