# ledger-app-store-api

This server manages Ledger application for BOLOS devices. It can get all
currently available applications for a given device. And provide all information
to install/uninstall them as long as informations.

Setup
=====

1. Clone sources
2. [Install pipenv](https://github.com/pypa/pipenv#installation)

How to run
==========

1. Go to sources directory
2. Activate python virtual environment by running `pipenv shell`
3. Launch the application `python manage.py runserver`


# Local configuration

You can override the default configuration by creating a `ledger_app_store/local_settings.py`
It will be loaded after the default config and will allow change local setting like database or debug mode

Example :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_db_name',
        'USER': 'my_username',
        'PASSWORD': 'my_strong_password',
        'HOST': 'my_DB_host',
        'PORT': '3306',
    }
}

DEBUG = False
```

This file is being ignored by git
