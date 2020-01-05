"""
Django settings for ww project.
Generated by 'django-admin startproject' using Django 2.2.4.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qhh(ydahm&a&(z45^jpsk2v@r7q2h_-@furoe@&md=s#f5)-c&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['qc.sairanmed.ir', 'localhost']


# Application definition

INSTALLED_APPS = [
    'form.apps.FormConfig',
    'acc.apps.AccConfig',
    'report.apps.ReportConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
]



"""
EMAIL_BACKEND= "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST= "smtp.gmail.com"
EMAIL_HOST_USER= "bdgjmwtp13@gmail.com"
EMAIL_HOST_PASSWORD= "Pass123654"
EMAIL_PORT= 587
EMAIL_USE_TLS= True
DEFAULT_FROM_EMAIL= "bdgjmwtp13@gmail.com"
"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'qc.sairanmed.ir'
EMAIL_USE_TLS = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'noreply@qc.sairanmed.ir'
EMAIL_HOST_PASSWORD = '^=TYWtYv$&D0'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ww.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['ww/templates'],
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

WSGI_APPLICATION = 'ww.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'kaadir_ASE',
        'PASSWORD': 'uJHP_bpK9bN+',
        'PORT': '5432',
        'USER': 'kaadir_ASE_admin',
    }
}
LOGIN_URL = '/'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/


LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static/')
# STATIC_ROOT = '/home/kaadcoir/public_html/qc/static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'ww/static/'),
]

MEDIA_ROOT = os.path.join(BASE_DIR,'static/media')
# MEDIA_URL = '/sta/'


SESSION_EXPIRE_AT_BROWSER_CLOSE = True
DEBUG_PROPAGATE_EXCEPTIONS = True
