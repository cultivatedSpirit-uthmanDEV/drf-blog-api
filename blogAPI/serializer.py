from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post= serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = [
            'user'
            'post'

        ]



class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    like = LikeSerializer(read_only = True)
    class Meta:
        model = Post
        fields = [
                'user',
                'category',
                'title' , 
                'content' ,
                'like_count'
                'created_at', 
                'updated_at', 
                'published'
        ]


    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "title cannot not be less than three"
            )
        return value


    def title(self, value):
        if Post.objects.filter(title = value).exists():
            raise serializers.ValidationError(
            "title already exist")

    def get_like_count(self, obj):
        return obj.like.count()



class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post= serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'post',
            'content',
            'created_at',
            #'updated_at',
        ]









  
            

    

   