from django.urls import path

from .views import sign_up_form, user_login, render_user

urlpatterns = [

    path('sign/', sign_up_form, name='sign'),

    path('login/', user_login, name='login'),

    path('profile/<int:id>/', render_user, name="profile")

]
