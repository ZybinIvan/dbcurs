from django.urls import path

from .views import func_super_puper

urlpatterns = [

    path('<int:id>', func_super_puper, ),



]
