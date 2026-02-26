"""
This file contains the forms for the notes app.
It will handle the logic for creating and updating notes.
"""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and updating Note objects.

    Fields:
    - title: CharField for the note title.
    - body: TextField for the note body.

    Meta class:
    - Defines the model to use (Note) and the fields to include in the form.

    :param forms.ModelForm: Django's ModelForm class.
    """

    class Meta:
        model = Note
        fields = ["title", "body"]
