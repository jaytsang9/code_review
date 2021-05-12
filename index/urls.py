from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('py_reviews', views.py_reviews, name='py_reviews'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]