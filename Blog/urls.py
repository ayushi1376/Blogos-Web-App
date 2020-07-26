from django.contrib import admin
from django.urls import path,include
from blog import views


urlpatterns = [
    #API to post a comments
    path('postComment',views.postComment, name='postComment'),
    
    path('', views.blogHome, name='Bloghome'),
    path('<str:slug>', views.blogPost, name='blogPost'),

    

]
