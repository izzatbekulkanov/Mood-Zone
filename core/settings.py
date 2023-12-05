import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z=wwe6i7-o7*g5r2@z%7u4egmb_wzp(cxhk#ry-m=&k-ylx%dd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

# Mahalliy ilovalar (local apps)
LOCAL_APPS = [
    'landing_page',
    'dashboard',
    'users',
    'social',
    'mail',
    'ecommerce',
    'appointment',
    'blog',
    'file_manager',
    'chat',
    'API',
]

# Umumiy ilovalar (django.contrib va boshqa global ilovalar)
GLOBAL_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.utils.translation',
]

INSTALLED_APPS = LOCAL_APPS + GLOBAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Asosiy template katalogi
            BASE_DIR / 'social',  # Social ilova template katalogi
            BASE_DIR / 'landing_page',  # Landing Page ilova template katalogi
            BASE_DIR / 'mail',  # Mail ilova template katalogi
            BASE_DIR / 'ecommerce',  # E-commerce ilova template katalogi
            BASE_DIR / 'appointment',  # Appointment ilova template katalogi
            BASE_DIR / 'blog',  # Blog ilova template katalogi
            BASE_DIR / 'file_manager',  # File Manager ilova template katalogi
            BASE_DIR / 'chat',  # Chat ilova template katalogi
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# settings.py
AUTH_USER_MODEL = 'users.CustomUser'

AUTHENTICATION_BACKENDS = [
    'users.custom_backend.CustomBackend',
    'django.contrib.auth.backends.ModelBackend',
]
# Jazzmin settings

JAZZMIN_SETTINGS = {
    # oynaning sarlavhasi (masofada yoki None bo'lsa, current_admin_site.site_title bo'lmaganda)
    "site_title": "Kutubxona Admin",

    # Kirish ekranidagi sarlavha (19 belgidan ko'proq bo'lmasa,
    # current_admin_site.site_header bo'lmaganda yoki None bo'lsa)
    "site_header": "Kutubxona",

    # Logotip (brand) uchun, static fayllarda bo'lishi kerak, o'ng yuqori burchakda ishlatiladi
    "site_logo": "books/img/logo.png",

    # Kirish forma logotipi uchun (agar mavjud bo'lsa, site_logo bo'lmaganda)
    "login_logo": None,

    # Tungi mavzularda kirish formasidagi logotip uchun (login_logo bo'lmaganda)
    "login_logo_dark": None,

    # Logotipning ustiga qo'yiladigan CSS klasslari
    "site_logo_classes": "img-circle",

    # Saytingiz uchun faviconning o'rtacha manzili (masofada bo'lmaganda site_logo
    # bo'lganda avtomatik o'rnatiladi, ideal ravishda 32x32 piksel)
    "site_icon": None,

    # Kirish ekranidagi xush kelibsiz matn
    "welcome_sign": "Kutubxonaga xush kelibsiz",

    # Pastkisamdagi mualliflik huquqi
    "copyright": "Acme Kutubxona Ltd",

    # Qidiruv panelidan izlanadigan model adminlar ro'yxati, agar bekor qilingan bo'lsa qidiruv paneli o'chiriladi
    # Agar faqatgina bir qidiruv maydonini ishlatmoqchi bo'lsangiz,
    # ro'yxat ishlatish kerak emas, oddiy matn ishlatishingiz mumkin
    "search_model": ["auth.User", "auth.Group"],

    # Foydalanuvchi modelida avatarning yo'nalishi ImageField/URLField/Charfield
    # yoki foydalanuvchini qabul qiladigan funktsiya
    "user_avatar": None,

    ############
    # Yuqori Menyu #
    ############

    # Yuqori menyuga joylashtiriladigan havolalar ro'yxati
    "topmenu_links": [

        # Qaytarib olinadigan URL (Ruxsatlar qo'shilgan)
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},

        # Yangi oynada ochadigan tashqi URL (Ruxsatlar qo'shilgan)
        {"name": "Qo'llab-quvvatlash", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # Qidiruv paneliga bog'liq model admin
        {"model": "auth.User"},

        # Drop-down menyuga ega bo'lgan barcha model sahifalari uchun ilova
        {"app": "books"},
    ],

    #############
    # Foydalanuvchi Menyu #
    #############

    # Yuqori o'ng tarafdagi foydalanuvchi menyusiga qo'shiladigan qo'shimcha
    # havolalar ro'yxati ("app" url turi mumkin emas)
    "usermenu_links": [
        {"name": "Qo'llab-quvvatlash", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Yon Menu #
    #############

    # Yon menyuni ko'rsatish yoki ko'rsatmaslik
    "show_sidebar": True,

    # Menyuni avtomatik kengaytirish yoki emas
    "navigation_expanded": True,

    # Bu ilovalarni menyuni yaratishda yashirish (masalan, auth)
    "hide_apps": [],

    # Bu modellarni menyuni yaratishda yashirish (masalan, auth.user)
    "hide_models": [],

    # Menyuning tartibini belgilash uchun ilova (va/yoki modellardan)
    # ro'yxati (barcha ilovalar/modellarga ega bo'lishi kerak emas)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # App guruhi yaratish uchun qo'shimcha havolalar ro'yxati, ilova nomi boyicha
    "custom_links": {
        "books": [{
            "name": "Xabar yaratish",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # to'liq 5.13.0 bepul ikon klasslarining ro'yxati uchun
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Qo'l tartibida keltirilgan ikonlar
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Bog'liq Modal #
    #################
    # Popupalarni o'rnatingan chiqish modalini ishlatish
    "related_modal_active": False,

    #############
    # UI Ozgartirishlari #
    #############
    # Ma'lumotlar static fayllarda bo'lishi kerak bo'lgan moslashuv CSS/JS skriptlarining
    # o'rtacha manzillari (masofada bo'lsa, None bo'lishi kerak)
    "custom_css": None,
    "custom_js": None,
    # fonts.googleapis.com manzilidan fontni ulashmoqchi bo'lsangiz (faqat ishlatilmasa,
    # custom_css orqali fontni taqdim etishingiz mumkin)
    "use_google_fonts_cdn": True,
    # Yuqori o'ng tarafdagi UI moslashuvchini ko'rsatish yoki ko'rsatmaslik
    "show_ui_builder": False,

    ###############
    # Ko'rishni O'zgartirish #
    ###############
    # O'zgartirishni bitta shaklda ko'rsatish, yoki tablar ichida (hozirgi tanlovlar)
    # - single
    # - horizontal_tabs (oddiy tanlov)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # modeladmin asosida o'zgartirish formatini o'zgartirish
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Admin paneldagi til tanlovini qo'shish
    "language_chooser": False,
}
