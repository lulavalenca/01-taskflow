"""Views for the TaskFlow REST API."""

from rest_framework import generics

from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    """List all tasks and create a new task."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a task."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
