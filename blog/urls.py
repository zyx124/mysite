from django.urls import path, include
from django.contrib import admin

import blog
from . import views


# add a name space in case mixed with other namespaces
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('category/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
    path('contact/', views.contact, name='contact'),
]