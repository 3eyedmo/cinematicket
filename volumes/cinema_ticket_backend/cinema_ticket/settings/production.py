from .base import *
from datetime import timedelta

SECRET_KEY = "django-insecure-oa9a_m&_8wf0-f_d2yl=vd_^fr^i5&bc-#ubne0^(4$mzupg6s"
DEBUG = False

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_CREDENTIALS = True 
CORS_ALLOWED_ORIGINS = [
    "http://154.91.170.66:3000",
]
CSRF_TRUSTED_ORIGINS = [
    "http://154.91.170.66:3000",
]

CSRF_USE_SESSIONS = False
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

