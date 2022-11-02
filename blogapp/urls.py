from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('/browse',browse),
    path('/viewblog',viewblog),
    path('/createblog',createblog),
    path('/submitblog',submitblog),
]
