from django.shortcuts import render
from rest_framework import generics
from blogAPI.models import Post
from blogAPI.serializer import PostSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class PostListCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    


list_create_view = PostListCreateAPIView.as_view()