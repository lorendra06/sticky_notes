"""
Models for the Sticky Notes application.
Defines the database schema for storing user notes.
"""

from django.conf import settings
from django.db import models


class Note(models.Model):
    """
    Model representing a sticky note.

    Fields:
        - title: CharField for the note title with a maximum
                length of 100 characters.
        - body: TextField for the note body.
        - created_at: DateTimeField set to the current date
                    and time when the note is created.
    Relationships:
        - author: ForeignKey representing the author of the note.
    """

    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes",
    )

    def __str__(self):
        """Returns the title as the string representation of the note."""
        return str(self.title)
