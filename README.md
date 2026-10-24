# Business website (Django, liquid glass theme)

Pages: Home, IoT projects, Website builds, About, Contact. No user login.

## Run it
    python -m venv venv
    venv\Scripts\activate        (Windows)   |   source venv/bin/activate   (Mac/Linux)
    pip install -r requirements.txt
    python manage.py makemigrations core
    python manage.py migrate
    python manage.py seed                # optional sample projects
    python manage.py createsuperuser     # only for YOU to use /admin/
    python manage.py runserver

Open http://127.0.0.1:8000

## Customise
- Business name, email, phone, WhatsApp, social links: `config/settings.py` -> BRAND
- Add / edit projects with photos, and read contact messages: http://127.0.0.1:8000/admin/
- Colours and glass look: `core/static/core/css/style.css` (variables at the top)

## Before going live
Set DEBUG = False, a real SECRET_KEY and ALLOWED_HOSTS, then run `python manage.py collectstatic`.
