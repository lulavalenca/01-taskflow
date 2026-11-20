"""Django application configuration for tasks."""

from django.apps import AppConfig


class TasksConfig(AppConfig):
    """Application configuration for TaskFlow tasks."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.tasks"
    verbose_name = "Tarefas"
