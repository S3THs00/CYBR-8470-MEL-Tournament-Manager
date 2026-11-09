
# Midwest Esports League Tournament Manager

**CYBR-8470 — Software Architecture Project**

A Django-based esports tournament registration, check-in, and management application for Midwest Esports League (MEL).

## Project Overview

The Midwest Esports League Tournament Manager is a web application designed to simplify the organization and management of esports tournaments.

The application allows players to create accounts, log in, view upcoming tournaments, and preregister for events. Administrators can create tournaments, review player registrations, track attendance, and manually confirm payments.

The goal is to create a simple, reliable, and secure system that improves the tournament experience for both players and organizers.

This repository contains the initial working prototype developed for CYBR-8470.

## Implemented Features

The current prototype includes:

- Player account creation and login
- Tournament creation and management through Django Admin
- Tournament listing with dates, locations, and player limits
- Player preregistration for tournaments
- Duplicate-registration prevention
- Registration status and confirmation messages
- Manual player check-in tracking through Django Admin
- Manual payment confirmation through Django Admin
- Django authentication and password hashing
- CSRF protection for registration forms
- SQLite database storage

## Planned Features

Future development may include:

- Dedicated tournament organizer dashboard
- Improved player registration status display
- Tournament capacity enforcement
- Priority check-in management
- Enhanced role-based access controls
- Additional security and input validation
- Improved player profiles and tournament history
- PostgreSQL database support
- Docker containerization

## Technologies

### Current Prototype

- Python 3.13
- Django
- SQLite
- HTML
- CSS
- Git and GitHub
- python-dotenv

### Planned Technologies

- PostgreSQL
- Docker

## Installation

The MEL Tournament Manager is built with Python and Django. The current prototype uses SQLite for local database storage.

### Prerequisites

Before installing the application, ensure that you have:

- Python 3.13 or a compatible version
- Git
- A terminal such as Windows PowerShell
- An internet connection to download Python dependencies

### 1. Clone the Repository

Open Windows PowerShell and run:

```powershell
git clone https://github.com/S3THs00/CYBR-8470-MEL-Tournament-Manager.git
cd CYBR-8470-MEL-Tournament-Manager
```

### 2. Create a Virtual Environment

Create a Python virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the required Python packages:

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a file named `.env` in the project root directory.

Generate a unique Django secret key using:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated value into the `.env` file using this format:

```dotenv
DJANGO_SECRET_KEY=your-generated-secret-key
```

Replace `your-generated-secret-key` with your actual generated value.

**Security:** Never commit the `.env` file or share your secret key publicly. The project is configured to exclude `.env` from Git tracking.

### 5. Initialize the Database

Apply the Django database migrations:

```powershell
python manage.py migrate
```

This creates the SQLite database and the tables required by the application.

The application is now installed and ready to run.

## Getting Started

After completing the installation steps, you can start and use the MEL Tournament Manager locally.

### 1. Start the Development Server

Open Windows PowerShell in the project directory.

If your virtual environment is not active, activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Start the Django development server:

```powershell
python manage.py runserver
```

Open your browser and navigate to:

http://127.0.0.1:8000/

The application will redirect you to the player login page.

### 2. Create a Player Account

On the login page:

1. Click **Create Account**.
2. Enter a username and password.
3. Confirm your password.
4. Click **Create Account**.

After successful account creation, you will be logged in automatically and redirected to the tournament listing.

### 3. Create an Administrator Account

To manage tournaments, first create an administrator account.

Open a separate Windows PowerShell terminal in the project directory and activate the virtual environment.

Run:

```powershell
python manage.py createsuperuser
```

Follow the prompts to create an administrator username and password.

Navigate to:

http://127.0.0.1:8000/admin/

Log in using the administrator account.

### 4. Create a Tournament

In Django Admin:

1. Select **Tournaments**.
2. Click **Add Tournament**.
3. Enter the tournament name, start date and time, location, and maximum number of players.
4. Enable registration if players should be allowed to preregister.
5. Save the tournament.

The tournament will appear on the tournament listing page.

### 5. Preregister for a Tournament

While logged in as a player:

1. Navigate to http://127.0.0.1:8000/tournaments/
2. Find a tournament with open registration.
3. Click **Preregister**.
4. Review the confirmation message.

The application prevents the same player account from registering for the same tournament more than once.

**Important:** Preregistration does not guarantee a tournament spot. Players must complete check-in and payment confirmation with the organizer.

For MEL events, preregistered players receive priority during the first 15 minutes of the check-in window. Remaining spots become available to walk-in players during the final 15 minutes. This scheduling policy is not yet automated in the prototype.

### 6. Manage Registrations

Administrators can review player registrations through Django Admin.

1. Navigate to http://127.0.0.1:8000/admin/
2. Select **Registrations**.
3. Select a player registration.
4. Update the **Checked in** and **Payment confirmed** fields as appropriate.
5. Save the changes.

Check-in and payment confirmation are handled manually in the current prototype.

### 7. Stop the Development Server

Return to the Windows PowerShell terminal running Django.

Press **Ctrl + C** to stop the development server.

## Security Considerations

The prototype includes several security controls:

- Django's built-in authentication system
- Secure password hashing
- CSRF protection for submitted forms
- Authenticated access to player preregistration
- Database constraints preventing duplicate registrations
- Environment-variable storage for the Django secret key
- Administrative access controls through Django Admin

Additional security features, including enhanced role-based access controls, rate limiting, and production deployment hardening, are planned for future development.

The application currently runs in a local development environment and is not configured for production deployment.

## Project Documentation

Additional project documentation is available in the `docs` directory, including interface mockups and C4 architecture diagrams.

The architecture documentation includes:

- C4 Level 1 — System Context Diagram
- C4 Level 2 — Container Diagram
- C4 Level 3 — Component Diagram

## License

See the `LICENSE` file in the repository for licensing information.

