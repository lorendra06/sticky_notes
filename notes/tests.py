"""
Tests for the Sticky Notes application.
Covers Models, CRUD operations, and User Authentication.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Note

# Get the User model dynamically to satisfy Pylint
User = get_user_model()


class NoteModelTest(TestCase):
    """Test cases for the Note database model."""

    def setUp(self):
        """Set up dynamic users and notes for testing."""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword123"
        )
        self.note = Note.objects.create(
            title="Dynamic Test Note",
            body="This is a test body.",
            author=self.user,
        )

    def test_note_has_title(self):
        """Test that a Note object has the expected title."""
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, "Dynamic Test Note")

    def test_note_has_body(self):
        """Test that a Note object has the expected body."""
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.body, "This is a test body.")

    def test_note_model_string_representation(self):
        """Test if the __str__ method returns the title."""
        self.assertEqual(str(self.note), self.note.title)


class NoteViewTest(TestCase):
    """Test cases for Note-related views (CRUD operations)."""

    def setUp(self):
        """Set up the environment with minimal instance attributes."""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword123"
        )
        self.other_user = User.objects.create_user(
            username="otheruser", password="otherpassword123"
        )
        self.note = Note.objects.create(
            title="Dynamic Test Note",
            body="This is a test body.",
            author=self.user,
        )

    def test_note_list_view(self):
        """Test the note board (Read List) for the logged-in user."""
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)

    def test_note_detail_view(self):
        """Test viewing a specific note's content."""
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(reverse("note_detail", args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.body)

    def test_note_create_view(self):
        """Test the creation of a new note via POST request."""
        self.client.login(username="testuser", password="testpassword123")
        new_note_data = {"title": "New Note", "body": "Content of the note."}
        response = self.client.post(reverse("note_create"), new_note_data)
        self.assertRedirects(response, reverse("note_list"))
        self.assertEqual(Note.objects.count(), 2)

    def test_note_update_view(self):
        """Test updating an existing note and checking database persistence."""
        self.client.login(username="testuser", password="testpassword123")
        updated_data = {"title": "Updated", "body": "Updated content."}
        response = self.client.post(
            reverse("note_edit", args=[self.note.id]), updated_data
        )
        self.assertRedirects(
            response,
            reverse(
                "note_detail",
                args=[self.note.id],
            ),
        )
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated")

    def test_note_delete_view(self):
        """Test deleting a note and verifying removal."""
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.post(
            reverse(
                "note_delete",
                args=[self.note.id],
            ),
        )
        self.assertRedirects(response, reverse("note_list"))
        self.assertEqual(Note.objects.count(), 0)

    def test_authorization_access_other_users_note(self):
        """Verify that a user cannot access another user's private note."""
        self.client.login(username="otheruser", password="otherpassword123")
        response = self.client.get(reverse("note_detail", args=[self.note.id]))
        self.assertEqual(response.status_code, 404)


class AuthenticationTest(TestCase):
    """Test cases for User Login and Registration."""

    def test_login_view(self):
        """Test that a user can log in with valid credentials."""
        User.objects.create_user(username="loginuser", password="password123")
        response = self.client.post(
            reverse("login"),
            {
                "username": "loginuser",
                "password": "password123",
            },
        )
        self.assertRedirects(response, reverse("note_list"))

    def test_registration_view(self):
        """Test that a new user can register and is auto-logged in."""
        registration_data = {
            "username": "newuser",
            "password1": "SecurePass123!",
            "password2": "SecurePass123!",
        }
        response = self.client.post(reverse("register"), registration_data)

        # Verify user was created in the database
        self.assertTrue(User.objects.filter(username="newuser").exists())
        # Verify redirect to dashboard after registration
        self.assertRedirects(response, reverse("note_list"))
