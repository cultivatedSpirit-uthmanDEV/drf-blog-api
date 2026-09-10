from django.shortcuts import render
from rest_framework import generics
from blogAPI.models import Post, Comment, Like
from blogAPI.serializer import PostSerializer, CommentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from permission import IsOwner
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
@permission_classes([IsAuthenticated, IsOwner])
def update(request, pk):
    instance = get_object_or_404(Post, pk=pk)

    if not IsOwner().has_object_permission(request, None, instance):
    #if request.user == instance.user:
       serializer = PostSerializer(instance, data= request.data, user = request.user, partial= request.method == 'PATCH' )
       if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)
# Not tested yet



# Comment View

# create comment

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, pk):
    serializer = CommentSerializer(data=request.data)
    post = get_object_or_404(Post, pk=pk)
    if serializer.is_valid():
        serializer.save(post=post,user=request.user)
    
        return Response({"Message" : "Commented succesfully"}, status=201)
    return Response(serializer.errors)


# list of comment 

@api_view(['GET'])
def post_comment_list(request, pk):
    post = Post.objects.get(pk=pk)
    comment_list = post.comment.all()
    serializer = CommentSerializer(comment_list, many=True)
    return Response(serializer.data)

#get a comment
@api_view(['GET'])
def comment_detail(request, pk, comment_pk):
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(
        Comment,
        pk=comment_pk,
        post=post
    )
    comment_instance = CommentSerializer(comment)
    return Response(comment_instance.data)

@api_view(['PATCH', 'PUT'])
def update_comment(request, pk, comment_pk):
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(
    Comment,
    pk=comment_pk,
    post=post
)

    serializer = CommentSerializer( comment, user= request.user,data = request.data, partial= request.method == 'PATCH')
    if serializer.is_valid():
        serializer.save(post=post, user=request.user)
        return Response({'message' : 'message updated!'})
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_comment(request, pk, comment_pk):
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_pk, post=post)

    comment.delete()

    return Response({'message' : 'Deletd!'})




# Like views
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.create(
        user=request.user,
        post=post
    )
     
    return Response(
        {"message": "Post liked successfully"},
        status=201
    )

# unlike a post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk, like_pk):
    post = get_object_or_404(Post, pk=pk)
    like = get_object_or_404(
           Like,
           pk=like_pk,
           post=post,
           user=request.user
    )

    like.delete()

    return Response({'message' : 'unliked successfully'})

    





