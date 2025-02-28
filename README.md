# Django Blog Post Project

## Overview
This is a simple blog application built with Django. Users can create and delete posts. Each post can be clicked to view more details, including:
- Full post content
- Author information
- Tags
- Similar posts
- Latest posts
- Comments section for user interaction

## Features
- **Create Post**: Users can create blog posts with a title, content, and tags.
- **Delete Post**: Users can delete their own posts.
- **View Post Details**: Click on a post to view its full content along with related details.
- **Similar Posts**: Suggestions based on tags.
- **Latest Posts**: Displays the most recent posts.
- **Comment System**: Users can leave comments on posts.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/django-blog.git
   cd django-blog
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser (optional, for admin access):
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/` in your browser.
- Log in or register to create and manage posts.
- Click on any post to view details and leave comments.

## Technologies Used
- Django
- SQLite (default, can be replaced with PostgreSQL or MySQL)
- Bootstrap (for styling, optional)

## Author
Developed by Richie Sayer

---
