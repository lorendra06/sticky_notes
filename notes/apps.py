"""
Configuration for the Notes application.
This module contains the AppConfig class for the notes app.
"""

from django.apps import AppConfig


class NotesConfig(AppConfig):
    """
    Configuration class for the 'notes' Django application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "notes"
