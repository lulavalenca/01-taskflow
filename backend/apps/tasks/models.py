"""Data models for task management."""

from django.db import models


class Task(models.Model):
    """A task with a status, priority, and optional due date."""

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pendente"
        IN_PROGRESS = "IN_PROGRESS", "Em andamento"
        COMPLETED = "COMPLETED", "Concluída"

    class Priority(models.TextChoices):
        LOW = "LOW", "Baixa"
        MEDIUM = "MEDIUM", "Média"
        HIGH = "HIGH", "Alta"

    title = models.CharField("título", max_length=255)
    description = models.TextField("descrição", blank=True)
    status = models.CharField(
        "status", max_length=20, choices=Status.choices, default=Status.PENDING
    )
    priority = models.CharField(
        "prioridade", max_length=10, choices=Priority.choices, default=Priority.MEDIUM
    )
    due_date = models.DateField("data de vencimento", blank=True, null=True)
    created_at = models.DateTimeField("criada em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizada em", auto_now=True)

    class Meta:
        """Metadata for Task model presentation and default ordering."""

        verbose_name = "tarefa"
        verbose_name_plural = "tarefas"
        ordering = ["-created_at", "-pk"]

    def __str__(self):
        """Return the task title as its readable representation."""

        return self.title
