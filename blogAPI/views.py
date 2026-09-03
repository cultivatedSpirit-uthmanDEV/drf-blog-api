from django.shortcuts import render
from rest_framework import generics
from blogAPI.models import Post
from blogAPI.serializer import PostSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


class PostListCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    


list_create_view = PostListCreateAPIView.as_view()

@api_view(["GET", "POST"])
def create_post(request):
    queryset = Post.objects.create(
        title= 'title',
        content = 'content'
    )

    serializer = PostSerializer(queryset)
    data = serializer.save(user=request.user)

    return Response(data)
