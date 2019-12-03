from django.urls import path, include
from django.contrib import admin
from . import views


# add a name space in case mixed with other namespaces
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail')

]