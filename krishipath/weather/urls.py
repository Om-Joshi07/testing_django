


from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
]
