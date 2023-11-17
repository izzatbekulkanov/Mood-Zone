import os
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j%^*y0krq5^-#3lggoecxw!d7ad_gqkab3t5w17&0w06+qf8+8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
DEFAULT_APPS = [    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    
    ]
LOCAL_APPS = [
    "dashboards",
    "apps",
    "layouts",
    "components",
    "pages"
    ]
THIRDPARTY_APPS = [
    # All Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Google Providers
    'multiselectfield',
]

INSTALLED_APPS = DEFAULT_APPS +LOCAL_APPS +THIRDPARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'moodzone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': ['crispy_forms.templatetags.crispy_forms_tags'],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    # `social auth` specific authentication methods, such as login by Google
    'social_core.backends.google.GoogleOAuth2',
]

CRISPY_TEMPLATE_PACK = 'bootstrap'
WSGI_APPLICATION = 'moodzone.wsgi.application'
BOOTSTRAP4 = {
    'include_jquery': True,  # jQuery-ni ham o'rnatish
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#  Messages customize

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}



# SMTP Configure
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.mailtrap.io"
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "51a7bd029959fb"
EMAIL_HOST_PASSWORD = "8d0f17cedb0466"
DEFAULT_FROM_EMAIL = "51a7bd029959fb"

#  All Auth Configurations

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "account_login"
ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'
# All Auth Forms Customization 

ACCOUNT_FORMS = {
    "login": "moodzone.forms.UserLoginForm",
    "signup": "moodzone.forms.UserRegistrationForm",
    "change_password": "moodzone.forms.PasswordChangeForm",
    "set_password": "moodzone.forms.PasswordSetForm",
    "reset_password": "moodzone.forms.PasswordResetForm",
    "reset_password_from_key": "moodzone.forms.PasswordResetKeyForm",
}

SOCIALACCOUNT_QUERY_EMAIL = True

#Social auth google key and secrect key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '891737966773-8cuk5f8jk7l8uo1vp6g0c0rorb3ra3tk.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


SITE_ID = 2

# Provider Configurations
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}