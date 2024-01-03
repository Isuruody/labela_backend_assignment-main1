## Project Setup

### Prerequisites
- Python 3.x
- Django
- Virtual Environment (Optional but recommended)

### Setup Guide
1. Install Django: `pip install django`
2. Create Django Project: `django-admin startproject project_name`
3. Create 'accounts' App: `python manage.py startapp accounts`
    - Add provided models, serializers, and views code to respective files
4. Create 'carparts' App: `python manage.py startapp carparts`
    - Add provided models, serializers, and views code to respective files
5. Update 'urls.py' in the main project folder: Add URL patterns for admin, apps, and API documentation
6. Include Apps URLs: Add 'carparts' and 'accounts' app URLs to the main 'urls.py'
7. Install drf-yasg: `pip install drf-yasg`
8. Add Swagger and Redoc URLs: Create endpoints for API documentation using `get_schema_view`
9. Include Documentation URLs: Add endpoints to the main 'urls.py'
10. Run Django Server: `python manage.py runserver`
11. Access the API: Navigate to `/api/swagger/` and `/api/redoc/` in your browser



## API Documentation

Access the API documentation:

- [Swagger](/api/swagger/)
- [Redoc](/api/redoc/)
