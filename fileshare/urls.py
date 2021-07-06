from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.listPage, name="listPage"),  
    path('/newPost', views.newPost, name="newPost"),  
    path('/updatePost/<str:pk>', views.updatePost, name="updatePost"),  
    path('/deletePost/<str:pk>', views.deletePost, name="deletePost"),
    path('/detailPage/<str:pk>', views.detailPage, name="detailPage"),  
    path('/myPosts', views.myPostsPage, name="myPostsPage"),
    path('/UserSpecifiedPosts/<str:author>', views.UserSpecifiedPosts, name="UserSpecifiedPosts"),  
] 
