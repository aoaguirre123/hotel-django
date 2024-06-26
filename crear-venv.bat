call rmdir /S /Q .venv
call python -m venv .venv
call .venv\Scripts\activate
echo El entorno virtual de Python ha sido creado y activado.
call pip install -r requirements.txt