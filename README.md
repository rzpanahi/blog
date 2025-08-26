# Django Markdown Blog

**A simple, production-ready Django blog with taggit, markdown, comments, pagination and post sharing.**

> This repository contains a blog built with Django, using `django-taggit` for tags, the `markdown` library for writing posts, Django templates for rendering, and extra features such as comments, post sharing by email, pagination, custom filters, and sitemap support.


## Features

-   Django-powered blog with Markdown support for posts
    
-   Tagging via `django-taggit`
    
-   Comment system (with moderation)
    
-   Pagination for post lists
    
-   Post sharing via email
    
-   Custom filters and tag views
    
-   Sitemap generation for posts and tags
    
-   Clean Django templates and responsive UI
    

----------

## Tech stack

-   Python 3.10+ (recommended)
    
-   Django 5.x (or compatible)
    
-   PostgreSQL (recommended for production)
    
-   Nginx + Gunicorn (production)
    
-   Optional: Docker + Docker Compose
    

----------

## Getting started (local development)

### Prerequisites

-   Python 3.10+
    
-   pip
    
-   (Optional) PostgreSQL if you don't want SQLite locally
    

### Quick start

```bash
# clone
git clone https://github.com/rzpanahi/blog.git
cd blog

# create virtualenv and activate
python3 -m venv .venv
source .venv/bin/activate

# install
pip install -r requirements.txt

# copy example env
cp .env.example .env
# edit .env to set SECRET_KEY, DATABASE_URL (or SQLite), DEBUG=1 for dev

# run migrations and create superuser
python manage.py migrate
python manage.py createsuperuser

# collect static for dev (optional)
python manage.py collectstatic --noinput

# run dev server
python manage.py runserver

```

Open `http://127.0.0.1:8000/` in your browser.

----------

## Environment variables (.env example)

Create a `.env` file in the project root (use `django-environ` or `python-decouple` in settings):

```
# .env.example
SECRET_KEY="django-insecure-n&3uu3qrbq08dyf=95f^*po3gj30i1i+p8k$$lxas+&1$-4yn_"
DEBUG=True
EMAIL_HOST_USER=<your email>
EMAIL_HOST_PASSWORD=<your email host password>
DEFAULT_FROM_EMAIL=Reza Panahi's Blog <your email>
```