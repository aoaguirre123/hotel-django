call C:\ProyectosDjango\WEB\.venv\Scripts\activate.bat
call python manage.py runscript -v3 eliminar_tablas
call rmdir /s /q C:\ProyectosDjango\WEB\hotel\migrations
call python manage.py makemigrations
call python manage.py migrate

