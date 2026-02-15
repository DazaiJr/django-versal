from .base import *

DEBUG = False

ALLOWED_HOSTS = [".vercel.app"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("PGDATABASE"),
        "USER": env("PGUSER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PGHOST"),
        "PORT": env("PGPORT", default="5432"),
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
