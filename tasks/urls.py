from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from tasks import views
from tasks.views import TasksAPIView, TasksDoneAPIView

urlpatterns = [
    path('', TasksAPIView.as_view(), name='tasks-index'),
    path('done/', TasksDoneAPIView.as_view(), name='tasks-done'),
]
