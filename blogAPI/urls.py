from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('list/', views.list_create_view, name= 'create_view'),
    path('create/', views.list_create_view, name= 'create_view'),
    path('get_post/<int:pk>/', views.get_post, name= 'getpost'), 
    path('delete/<int:pk>/', views.post_delete_view, name= 'delete'),
    path('post/<int:pk>/create/comment/', views.create_comment, name= 'create_comment'),
    path('post/<int:pk>/comment/list/', views.post_comment_list, name= 'post_comment_list'),
    path('post/<int:pk>/comment/<int:comment_pk>/', views.comment_detail, name= 'comment_detail'),
    path('post/<int:pk>/comment/<int:comment_pk>/update/', views.update_comment, name= 'update_comment'),
    path('post/<int:pk>/comment/<int:comment_pk>/delete/', views.delete_comment, name= 'delete_comment'),
    
    

]