from .base import *  # noqa

DEBUG = True
SECRET_KEY = env("DJANGO_SECRET_KEY", default='django-insecure-dev-key')

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# INSTALLED_APPS += ["debug_toolbar"]
# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
