from django.shortcuts import render
from rest_framework import generics
from blogAPI.models import Post, Comment
from blogAPI.serializer import PostSerializer, CommentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from django.shortcuts import get_object_or_404


# Create your views here.


# Post Views

#class-based view for creating post
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
list_create_view = PostListCreateAPIView.as_view()


class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
post_delete_view = PostDestroyAPIView.as_view()



# function based view for creating post
"""@api_view(["GET", "POST"])
def create_post(request):
    serializer = PostSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save(user= request.user)
    return Response(serializer.data, status=400)"""


def search_post(request):
    query = request.Get.get('q', '')
    post = Post.objects.filter(
        Q(title__icontain= query)
    )

    return Response(post)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post(request, pk):
      instance = get_object_or_404(Post, pk=pk)
      serializer = PostSerializer(instance)
      data =  serializer.data
      return Response(data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(instance, data= request.data, partial= request.method == 'PATCH' )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)



# Comment View


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['pk'])
        serializer.save(post=post, user=self.request.user)

comment_create_view = CommentListCreateAPIView.as_view()







