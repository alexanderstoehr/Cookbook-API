# Cookbook API

The project is a Django-based Cookbook API designed to manage and share culinary recipes. It utilizes Django Rest Framework for creating
RESTful APIs, supporting operations like listing, creating, updating, and deleting cookbooks. The API employs JWT for authentication,
ensuring that only authenticated users can perform certain actions. Cookbooks are the primary entities, with functionality to list a user's
own cookbooks and manage cookbooks through CRUD operations. The project is structured to support scalability and secure access, with
considerations for production deployment, including static and media file management with Digitalocean Storage in a production environment.

- **Languages and Frameworks:**
    - Python
    - Django
    - Django Rest Framework

- **Authentication and Authorization:**
    - JWT (JSON Web Tokens) for authentication
    - `rest_framework_simplejwt` library for JWT handling

- **Database:**
    - Django ORM for database interactions

- **Static and Media Files Management:**
    - DigitalOcean Spaces for storage in production
    - `django-storages` and `boto3` for integration with DigitalOcean Spaces

- **Development Tools:**
    - PyCharm IDE
    - pip for package management

- **Other Libraries and Tools:**
    - `os` module for environment and file path handling
    - `datetime.timedelta` for setting JWT token lifetime