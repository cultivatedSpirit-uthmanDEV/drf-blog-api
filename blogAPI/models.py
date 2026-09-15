from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.TextField()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  =  models.DateTimeField(auto_now=True)
    published =  models.BooleanField(default=True)

    def __str__(self):
        return self.title
class Followers(models.Model):
     follower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="following")

     following = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="followers")

     created_at = models.DateTimeField(auto_now_add=True)



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment" )
    content = models.CharField(max_length= 500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.content

    

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name= "replies")
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    # add comment relation later

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    