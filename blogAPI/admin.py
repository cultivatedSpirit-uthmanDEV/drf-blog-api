from django.contrib import admin

# Register your models here.

from .models import Post , Comment

class PostAdmin(admin.ModelAdmin):
    #AuthorList = ['user']
    search_fields = ['title', 'content']
    post = ['title', 'content']
    

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    comment = ['content']
admin.site.register(Comment, CommentAdmin)