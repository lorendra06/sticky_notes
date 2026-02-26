"""
Admin configuration for the Sticky Notes application.
Registers models to the Django admin interface for management.
"""

from django.contrib import admin
from .models import Note

# Register your models here.
admin.site.register(Note)
