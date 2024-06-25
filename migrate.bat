call C:\ProyectosDjango\WEB\.venv\Scripts\activate.bat
call python manage.py makemigrations
call python manage.py makemigrations hotel
call python manage.py migrate
call python manage.py migrate hotel