from django.contrib import admin
from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.index, name='tasks-index'),
    path('done/', views.done, name='tasks-done'),
]
