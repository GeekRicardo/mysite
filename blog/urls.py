from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('article/<int:id>', views.article, name='article'),
    path('articles', views.articles, name='articlelist'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),



    path('load', views.load, name='load'),
    path('article', views.articledemo, name='articledemo'),
    path('test', views.test, name='test'),
    path('gettime', views.gettime, name='gettime'),
]
