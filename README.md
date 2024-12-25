
# My Blog Post

## Overview
This project is a Django-based web application that provides a blogging platform with the following features:

- View all articles on the homepage.
- View individual article details.
- Admin login for creating, updating, and deleting articles.
- Contact and About pages for additional information.

---

## Features

### 1. Homepage
- **URL:** `/`
- **Function:** Displays a list of all articles using the `home` view.
- **Template:** `index.html`
- **Context Variables:**
  - `data`: A list of articles retrieved from the database.

### 2. View Article
- **URL:** `/article/<p_id>`
- **Function:** Displays the details of a single article using the `article` view.
- **Template:** `post.html`
- **Context Variables:**
  - `id`: The ID of the article.
  - `post`: Article details retrieved from the database.

### 3. About Page
- **URL:** `/about`
- **Function:** Renders the About page using the `about` view.
- **Template:** `about.html`

### 4. Contact Page
- **URL:** `/contact`
- **Function:** Renders the Contact page using the `contact` view.
- **Template:** `contact.html`

### 5. Admin Login
- **URL:** `/admins`
- **Function:** Handles admin login functionality.
  - Validates the admin username and password.
  - If valid, redirects to the homepage with admin privileges.
  - If invalid, returns a `403 Forbidden` response.
- **Template:** `login.html`
- **Form:** `Login`

### 6. Create Article
- **URL:** `/create`
- **Function:** Handles the creation of new articles.
  - Displays a form to create an article.
  - On submission, saves the new article to the database.
  - If the form is invalid, returns a `404 Not Found` response.
- **Template:** `createPost.html`
- **Form:** `CreatePost`
- **Context Variables:**
  - `form`: The `CreatePost` form.
  - `mode`: Set to `'create'` to indicate creation mode.

### 7. Delete Article
- **URL:** `/delete/<p_id>`
- **Function:** Deletes an article based on its ID.
  - If successful, redirects to the homepage.
  - If unsuccessful, returns a `404 Not Found` response.

### 8. Update Article
- **URL:** `/update/<p_id>`
- **Function:** Updates an existing article based on its ID.
  - Displays a pre-filled form for the selected article.
  - Saves the updated details to the database on submission.
- **Template:** `createPost.html`
- **Form:** `CreatePost`
- **Context Variables:**
  - `form`: The `CreatePost` form pre-filled with article data.
  - `mode`: Set to `'update'` to indicate update mode.
  - `p_id`: The ID of the article being updated.

---

## Models
### Article
- Responsible for handling article-related operations such as retrieving, creating, updating, and deleting articles.

### Admins
- Handles admin authentication and verification.

---

## Forms
### Login
- A form for admin login, including fields:
  - `admin_name`
  - `password`

### CreatePost
- A form for creating and updating articles, including fields:
  - `title`
  - `subtitle`
  - `body`
  - `url`

---

## Setup

### Prerequisites
- Python 3.9+
- Django 4.2.15

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

---

## Future Improvements
- Add user authentication for non-admin users.
- Implement pagination for articles.
- Enhance the admin dashboard with more functionalities.
- Add unit and integration tests for views and forms.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements
- Django Documentation: https://docs.djangoproject.com
- Python Documentation: https://docs.python.org
https://roadmap.sh/projects/personal-blog
