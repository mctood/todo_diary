from django.contrib import admin
from django.urls import path

from notes import views

urlpatterns = [
    path('', views.index, name='notes-index'),
    path('archive/', views.archive, name='notes-archive'),
]
