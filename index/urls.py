from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('py_reviews', views.py_reviews, name='py_reviews'),
    path('js_reviews', views.py_reviews, name='py_reviews'),
    path('php_reviews', views.py_reviews, name='py_reviews'),
    path('java_reviews', views.py_reviews, name='py_reviews'),
    path('cpp_reviews', views.py_reviews, name='py_reviews'),
    path('c_reviews', views.py_reviews, name='py_reviews'),
    path('sql_reviews', views.py_reviews, name='py_reviews'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('review/<int:num>/', views.show_review, name='review'),
]