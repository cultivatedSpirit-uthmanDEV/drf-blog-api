from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Post
        fields = [
                'user',
                'title' , 
                'content' ,
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