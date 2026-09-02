from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_create_view, name= 'list_create_view')
]