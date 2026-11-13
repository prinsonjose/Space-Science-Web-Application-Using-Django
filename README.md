# Space-Science-Web-Application-Using-Django

## Project Description

**Space-Science-Web-Application-Using-Django** is a web-based space science blog application developed using the **Django** web framework. It allows visitors to explore space-related projects and blog articles, learn about the website, and send messages through a contact form.

The project uses an online website template as its starting point. The template was adapted and integrated with Django to add dynamic content, database management, and user authentication features.

## Features

- Home page with featured space projects and recent blog posts.
- Projects section to display space-related projects and descriptions.
- Blog section to browse articles and view individual posts.
- User registration, login, and logout.
- Login protection for individual blog posts and project details.
- Contact form for submitting messages.
- Django administration panel to manage projects, blog posts, and contact messages.
- Dynamic content stored in a MySQL database.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL
- **Template:** An online website template, customized and integrated with Django

## Project Structure

```text
Space-Science-Web-Application-Using-Django/
├── blog/              # Django project settings and main URL configuration
├── login_page/        # Registration, login, and logout functionality
├── space_blog/        # Blog, project, contact models and page views
├── static/            # CSS, JavaScript, and static images
├── templates/         # HTML templates
├── manage.py          # Django management utility
└── README.md
```

## Getting Started

### 1. Clone or download the project

```bash
git clone <repository-url>
cd Space-Science-Web-Application-Using-Django
```

If you downloaded the project as a ZIP file, extract it and open the project folder in your terminal.

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install the required packages

```bash
pip install django mysqlclient pillow
```

### 4. Configure the MySQL database

The project settings are configured to use a MySQL database named `blog` on `localhost`, with the username `root` and an empty password.

Create a database named `blog` in MySQL. If your MySQL username, password, host, or port is different, update the `DATABASES` configuration in `blog/settings.py` before running the application.

### 5. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create the admin account.

### 7. Run the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

The Django administration panel is available at:

```text
http://127.0.0.1:8000/admin/
```

## Notes

- Make sure MySQL is running and the database configuration is correct before starting the server.
- Add project and blog content through the Django administration panel.
- Uploaded project and blog images are stored in the media directory.
- This project is configured for local development. Before deploying it publicly, update the Django security settings, use a secure `SECRET_KEY`, configure `ALLOWED_HOSTS`, and set `DEBUG = False`.

## Credits

The website's frontend design is based on an online website template. It was adapted and integrated with Django as part of this project. The backend functionality, including dynamic content handling, database integration, and user authentication, is implemented using Django.
