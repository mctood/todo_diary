from django.contrib import admin
from django.urls import path

from notes import views
from notes.views import NotesAPIView

urlpatterns = [
    path('', NotesAPIView.as_view(), name='notes-index'),
    path('archive/', views.archive, name='notes-archive'),
    path('seek/<int:year>/<int:month>/<int:day>', views.seek, name='notes-seek'),
]
