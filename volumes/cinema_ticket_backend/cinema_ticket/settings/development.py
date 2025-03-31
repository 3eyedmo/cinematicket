from .base import *
from datetime import timedelta


SECRET_KEY = "This Is A Demo Project|dsmlkmdsaklmsadlksmadk"
DEBUG = False

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_CREDENTIALS = True 
CORS_ALLOWED_ORIGINS = [
    # "http://localhost:5173",  
    # "http://127.0.0.1:5173",  
    # "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",    
    "http://localhost:3000",
]
CSRF_TRUSTED_ORIGINS = [
    # "http://localhost:5173",
    # "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",    
    "http://localhost:3000",
]

CSRF_USE_SESSIONS = False
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}


