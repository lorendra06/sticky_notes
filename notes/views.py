"""
This file contains the views for the notes app.
It will handle the logic for creating, reading, updating, and deleting notes.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .models import Note
from .forms import NoteForm


@login_required
def note_list(request):
    """View to display all notes for the logged-in user."""
    notes = Note.objects.filter(author=request.user)
    return render(
        request,
        "notes/note_list.html",
        {"notes": notes, "page_title": "My Sticky Notes"},
    )


@login_required
def note_detail(request, note_id):
    """View to display the details of a specific note."""
    note = get_object_or_404(Note, id=note_id, author=request.user)
    return render(request, "notes/note_detail.html", {"note": note})


@login_required
def note_create(request):
    """View to handle the creation of a new note."""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user  # Assign the logged-in user as author
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


@login_required
def note_update(request, note_id):
    """View to handle the update of an existing note."""
    note = get_object_or_404(Note, id=note_id, author=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            # Corrected: Added note_id to redirect
            return redirect("note_detail", note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


@login_required
def note_delete(request, note_id):
    """View to handle the deletion of an existing note."""
    note = get_object_or_404(Note, id=note_id, author=request.user)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "notes/note_delete_confirm.html", {"note": note})


def register(request):
    """View to handle user registration."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after registration
            return redirect("note_list")
    else:
        form = UserCreationForm()
    return render(request, "notes/register.html", {"form": form})
