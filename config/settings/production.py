from .base import *
import os
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

CSRF_TRUSTED_ORIGINS = [
    f"https://{host}" for host in ALLOWED_HOSTS if host
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Ensure Cloudinary is used for media storage
# If Cloudinary env vars are not set, this will fail, which is correct
# as Railway doesn't support local media file serving
