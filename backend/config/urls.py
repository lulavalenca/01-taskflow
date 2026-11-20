"""Root URL configuration for the TaskFlow backend."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.tasks.urls")),
]
