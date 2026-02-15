from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

CSRF_TRUSTED_ORIGINS = [
    "https://django-versal-production.up.railway.app",
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
