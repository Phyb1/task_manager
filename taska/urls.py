from django.urls import path, include
from django.contrib.auth import views as auth_views
from .import views

app_name = 'taska'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
]
