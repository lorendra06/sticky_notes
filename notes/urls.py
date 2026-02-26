"""
URL configuration for the Sticky Notes application.
Defines the mapping between URLs and views
for authentication and note management.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    note_list,
    note_detail,
    note_create,
    note_update,
    note_delete,
    register,
)

urlpatterns = [
    # --- Auth URLs ---
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="notes/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    # --- Note URLs ---
    # List all notes
    path("", note_list, name="note_list"),
    # Detail of a specific note
    path("note/<int:note_id>/", note_detail, name="note_detail"),
    # Create a new note
    path("note/create/", note_create, name="note_create"),
    # Update/Edit a note (Matches 'note_edit' in templates)
    path("note/<int:note_id>/update/", note_update, name="note_edit"),
    # Delete a note
    path("note/<int:note_id>/delete/", note_delete, name="note_delete"),
]
