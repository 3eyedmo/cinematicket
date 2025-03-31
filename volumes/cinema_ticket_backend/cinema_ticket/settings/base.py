from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
AUTH_USER_MODEL = "users.CinemaTicketUser"

MY_APPS = [
    "drf_spectacular",
    "rest_framework",
    "rest_framework_simplejwt",
    "helpers",
    "movies",
    "rooms",
    "users",
    "bookings",
    "corsheaders",
]

# Django Application + Project Packages And Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *MY_APPS
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware", 
    "corsheaders.middleware.CorsMiddleware", 
    "django.contrib.sessions.middleware.SessionMiddleware", 
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware", 
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "cinema_ticket.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "cinema_ticket.wsgi.application"


# Database Definition

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


REST_FRAMEWORK = {
    # Authentication settings
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # Optional settings
    'COMPONENT_SPLIT_REQUEST': True,  # Useful for file uploads
    'SCHEMA_PATH_PREFIX': '/api/',    # Adjust if your API is prefixed
}

# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, images)
STATIC_URL = "/static/"

# The directory where static files are collected during 'collectstatic'
STATIC_ROOT = BASE_DIR.parent / "staticfiles"

# Location to collect static files for production
STATICFILES_DIRS = [
    BASE_DIR.parent / "static",
]



MEDIA_URL = "/media/"  # The URL path to access media files
MEDIA_ROOT = BASE_DIR.parent / "media"  # Directory where media files will be stored

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"