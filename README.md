📌 Sticky Notes Application
A web-based application designed to help users create, manage, and organize their digital sticky notes. This project features a full authentication system and a responsive interface built with Django and Bootstrap 5.

🚀 Getting Started
Follow these steps to get the application running on your local machine:

1. Prerequisites
For prerequired software see requirements.txt file from the main folder.

2. Setup
Clone or download the project folder.

Open a terminal in the project's root directory.

Apply migrations to set up the database:

Bash
python manage.py migrate
Start the development server:

Bash
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/.

🔐 Authentication Guide
The application uses the @login_required decorator to protect user data, ensuring that you can only see and manage your own notes.

How to Create an Account
On the home page, you will be redirected to the Login screen if not authenticated.

Click on the "Create one here" or "Register here" link at the bottom of the card.

Fill in the Registration form:

Username: A unique name for your account.

Password: Must meet the security requirements listed on the page.

Click Sign Up. You will be automatically logged in and redirected to your personal dashboard.

How to Log In
Navigate to the /login/ URL.

Enter your credentials.

Upon success, you will be redirected to your Note List.

How to Log Out
While logged in, you will see a Logout button in the top navigation bar next to your username.

Click the button to securely end your session.

📝 Features
User-Specific Content: Each user sees only the notes they created.

Full CRUD: Create, Read, Update, and Delete notes with ease.

Responsive Design: Styled with a "Post-it" aesthetic using custom CSS and Bootstrap.

🛠️ Built With
Django: The web framework used.

Bootstrap 5: For responsive components and layout.

Google Fonts: 'Poppins' for UI and 'Reenie Beanie' for note content.

🔑 Admin Access (Superuser)
Django offers a built-in administration interface to manage all database records (Users and Notes).

Create a Superuser:
In your terminal, run:

Bash
python manage.py createsuperuser
Follow the Prompts: Enter a username, email, and a strong password.

Access the Panel:
Navigate to http://127.0.0.1:8000/admin/ and log in with your new credentials.

Management: From here, you can manually view, edit, or delete any note or user profile in the system.

📂 Project Structure
base.html: The main layout file containing the Bootstrap 5 CDN and the navigation logic for authenticated users.

views.py: Contains the core logic for Note CRUD operations and the Registration process.

styles.css: Custom styling for the "Sticky Note" yellow card effect and form layouts.

templates/notes/: Directory containing specific HTML files for Login, Register, and Note management.