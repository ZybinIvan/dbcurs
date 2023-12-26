from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import render_article, render_start, create_article, delete_article

urlpatterns = [

    path('<int:id>', render_article, ),

    path('', render_start, name='start'),

    path('article/<int:pk>/', render_article, name='article_detail'),

    path('create/', create_article, name='create'),

    path('delete-article/<int:id>', delete_article, name='delete'),

]
