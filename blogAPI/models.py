from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  =  models.DateTimeField(auto_now=True)
    published =  models.BooleanField()

class Category(models.Model):
    post = models.ManyToManyField(Post)
    name = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE )
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    