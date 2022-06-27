from django.urls import path

from .views import daily_task_progress

urlpatterns = [
    path("task_and_project/" , daily_task_progress)
]
