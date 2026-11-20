"""URL configuration for the tasks application."""

from django.urls import path

from apps.tasks.views import TaskDetailView, TaskListCreateView

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]
