from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('token', views.token),
    path('user', views.user),
    path('menu', views.menu),
]
