# Core LMS

A learning management system.

# Get Started

Start a project:

```shell
django-admin startproject mysite
cd mysite
```

Clone the repo:

```bash
git clone https://github.com/youzarsiph/core_lms.git
```

Install core_lms, in `mysite/settings.py`:

```python
INSTALLED_APPS = [
    'core_lms',  # Add this line
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Include `urls.py` from the core_lms, in `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include  # import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_lms.urls')),  # Add this line
]
```

Run migrate command:

```bash
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```

I hope that you find this useful. Thanks for your time.
