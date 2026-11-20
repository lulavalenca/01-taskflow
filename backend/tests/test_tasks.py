"""Tests for the Task model."""

from datetime import date

import pytest
from apps.tasks.models import Task

pytestmark = pytest.mark.django_db


def test_task_creation_sets_default_values():
    task = Task.objects.create(title="Prepare project plan")

    assert task.title == "Prepare project plan"
    assert task.status == Task.Status.PENDING
    assert task.priority == Task.Priority.MEDIUM
    assert task.description == ""
    assert task.due_date is None
    assert task.created_at is not None
    assert task.updated_at is not None


@pytest.mark.parametrize("status", Task.Status.values)
def test_task_accepts_each_status(status):
    task = Task.objects.create(title="Status test", status=status)

    assert task.status == status


@pytest.mark.parametrize("priority", Task.Priority.values)
def test_task_accepts_each_priority(priority):
    task = Task.objects.create(title="Priority test", priority=priority)

    assert task.priority == priority


def test_task_accepts_optional_fields():
    task = Task.objects.create(
        title="Optional fields",
        description="Additional details",
        due_date=date(2027, 1, 15),
    )

    assert task.description == "Additional details"
    assert task.due_date == date(2027, 1, 15)
