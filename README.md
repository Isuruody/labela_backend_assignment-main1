## Project Setup

### Prerequisites
- Python 3.x
- Django
- Virtual Environment (Optional but recommended)

### Setup Guide
1. Install Django: pip install django
2. You need to Install requiremnts.txt file (pip install -r requirements.txt)
3. Create Django Project: django-admin startproject project_name
4. Create 'accounts' App: python manage.py startapp accounts
    - Add provided models, serializers, and views code to respective files
5. Create 'carparts' App: python manage.py startapp carparts
    - Add provided models, serializers, and views code to respective files
6. Update 'urls.py' in the main project folder: Add URL patterns for admin, apps, and API documentation
7. Include Apps URLs: Add 'carparts' and 'accounts' app URLs to the main 'urls.py'
8. Install drf-yasg: pip install drf-yasg
9. Add Swagger and Redoc URLs: Create endpoints for API documentation using get_schema_view
10. Include Documentation URLs: Add endpoints to the main 'urls.py'
11. Run Django Server: python manage.py runserver
12. Access the API: Navigate to /api/swagger/ and /api/redoc/ in your browser



## API Documentation

Access the API documentation:

- [Swagger](/api/swagger/)
- [Redoc](/api/redoc/)


# Project Setup with Docker

### Prerequisites
- Docker installed on your machine
- docker build -t my_django_app .
- docker run -p 8080:8080 my_django_app

### Setup Guide
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <project_directory>
