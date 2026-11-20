"""Django admin configuration for tasks."""

from django.contrib import admin

from apps.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin list and filters for Task records."""

    list_display = ("title", "status", "priority", "due_date", "created_at")
    list_filter = ("status", "priority", "due_date")
    search_fields = ("title", "description")
    readonly_fields = ("created_at", "updated_at")
