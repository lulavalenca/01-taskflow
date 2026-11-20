"""Tests for the TaskSerializer."""

import pytest
from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer


@pytest.mark.django_db
def test_task_serializer_returns_expected_fields():
    task = Task.objects.create(
        title="Study Python",
        description="Practice Django Rest Framework",
    )

    serializer = TaskSerializer(instance=task)

    assert serializer.data["title"] == "Study Python"
    assert serializer.data["description"] == ("Practice Django Rest Framework")
    assert serializer.data["status"] == Task.Status.PENDING
    assert serializer.data["priority"] == Task.Priority.MEDIUM


@pytest.mark.django_db
def test_task_serializer_validates_new_task():
    data = {
        "title": "Build TaskFlow API",
        "description": "Create the REST API",
        "status": Task.Status.PENDING,
        "priority": Task.Priority.HIGH,
    }

    serializer = TaskSerializer(data=data)

    assert serializer.is_valid(), serializer.errors

    task = serializer.save()

    assert task.title == "Build TaskFlow API"
    assert task.priority == Task.Priority.HIGH


@pytest.mark.django_db
def test_task_serializer_read_only_fields():
    data = {
        "title": "Read only test",
        "id": 999,
    }

    serializer = TaskSerializer(data=data)

    assert serializer.is_valid(), serializer.errors

    assert "id" not in serializer.validated_data
