
# Django

## Overview

The Ashu-Django project is not just a typical project, but also a learning journey. Through this project, I have gained practical experience with various Django functionalities and best practices. It serves as a hands-on exploration of how to build and manage web applications using Django, while also honing my skills in Python.

## Installation

### Clone the Repository

Clone the project repository from GitHub and navigate into the project directory:

```bash
git clone https://github.com/yourusername/ashu-django.git
cd ashu-django
```

### Create a Virtual Environment

Create and activate a virtual environment to manage project dependencies:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install Dependencies

Install the required packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory and configure environment variables:

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

### Run Migrations

Apply database migrations to set up the initial database schema:

```bash
python manage.py migrate
```

### Create a Superuser

Create an administrative user to access the Django admin interface:

```bash
python manage.py createsuperuser
```

### Start the Server

Start the Django development server to run the project locally:

```bash
python manage.py runserver
```

Open your web browser and navigate to http://127.0.0.1:8000/ to view the project.

## Documentation

### Django Migrations

Migrations are Django’s method for propagating changes made to models into the database schema. They allow you to add or modify database tables and fields as your project evolves.

### Running Migrations

Apply migrations with the following command, which updates the database schema based on your migrations:

```bash
python manage.py migrate
```

### Creating Migrations

Generate new migrations when you make changes to your models:

```bash
python manage.py makemigrations
```

### Development Server

The `runserver` command starts a lightweight web server intended for development and testing. It is not suitable for production environments.

### Server Options

You can specify a different port or IP address for the server:

```bash
python manage.py runserver 0.0.0.0:8080
```

## Learning Progress

Throughout this project, I have focused on:

- Django Fundamentals: Deepened my understanding of Django’s core components, such as models, views, templates, and the admin interface.
- Migrations: Gained experience in managing database schema changes using Django migrations.
- Server Management: Learned to run and configure the Django development server effectively.
- Project Structure: Improved skills in organizing Django projects and adhering to best practices for setup and documentation.
