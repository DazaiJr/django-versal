from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

# Railway runs behind HTTPS proxy
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

# CSRF settings (THIS FIXES ADMIN LOGIN)
CSRF_TRUSTED_ORIGINS = [
    "https://*.railway.app",
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
