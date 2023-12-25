from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import render_article, render_start, sign_up_form, user_login

urlpatterns = [

    path('<int:id>', render_article, ),

    path('', render_start, name='start'),

    path('article/<int:pk>/', render_article, name='article_detail'),

    path('sign/', sign_up_form, name='sign'),

    path('login/', user_login, name='login'),
]
