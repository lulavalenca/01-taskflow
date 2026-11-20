"""Tests for the TaskFlow REST API."""

import pytest
from apps.tasks.models import Task
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_list_tasks():
    Task.objects.create(title="Study Python")

    client = APIClient()
    response = client.get("/api/tasks/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["title"] == "Study Python"


@pytest.mark.django_db
def test_create_task():
    client = APIClient()

    data = {
        "title": "Build TaskFlow API",
        "description": "Create REST endpoints",
        "status": Task.Status.PENDING,
        "priority": Task.Priority.HIGH,
    }

    response = client.post("/api/tasks/", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == "Build TaskFlow API"
    assert Task.objects.count() == 1


@pytest.mark.django_db
def test_retrieve_task():
    task = Task.objects.create(title="Study Django")

    client = APIClient()
    response = client.get(f"/api/tasks/{task.pk}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Study Django"


@pytest.mark.django_db
def test_update_task():
    task = Task.objects.create(title="Old title")

    client = APIClient()

    response = client.patch(
        f"/api/tasks/{task.pk}/",
        {"title": "Updated title"},
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK

    task.refresh_from_db()
    assert task.title == "Updated title"


@pytest.mark.django_db
def test_delete_task():
    task = Task.objects.create(title="Task to delete")

    client = APIClient()
    response = client.delete(f"/api/tasks/{task.pk}/")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Task.objects.filter(pk=task.pk).exists()
