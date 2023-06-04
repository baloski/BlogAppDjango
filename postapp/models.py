from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class User(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bio=models.TextField(null=True,blank=True)
    name=models.CharField(max_length=50)

class Comment(models.Model):
    comment_content=models.TextField(null=True,blank=True)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


class Block(models.Model):
    other_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='other_user')
    blocked_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='blocked_user')