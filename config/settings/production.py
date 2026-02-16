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

# Media files - set MEDIA_ROOT for potential fallback
MEDIA_ROOT = BASE_DIR / "media"

# Check if Cloudinary credentials are set, otherwise fall back to local storage
if not all([
    os.getenv("CLOUDINARY_CLOUD_NAME"),
    os.getenv("CLOUDINARY_API_KEY"),
    os.getenv("CLOUDINARY_API_SECRET")
]):
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
