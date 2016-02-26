from os import environ
from os.path import abspath, dirname, join, normpath
import sys

from django.conf import settings
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.shortcuts import render

from whitenoise.django import DjangoWhiteNoise


BASE_DIR = dirname(abspath(__file__))

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', 'localhost').split(',')
DEBUG = environ.get('DEBUG', '').lower() == 'true'
SECRET_KEY = environ.get('SECRET_KEY')


settings.configure(
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    DEBUG=DEBUG,
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.staticfiles',
    ),
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    ROOT_URLCONF=__name__,
    SECRET_KEY=SECRET_KEY,
    SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO', 'https'),
    STATIC_ROOT=normpath(join(BASE_DIR, 'public', 'static')),
    STATIC_URL='/static/',
    STATICFILES_DIRS=(
        normpath(join(BASE_DIR, 'static')),
    ),
    STATICFILES_STORAGE='whitenoise.django.GzipManifestStaticFilesStorage',
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [normpath(join(BASE_DIR, 'templates'))],
            'APP_DIRS': False,
            'OPTIONS': {
                'debug': DEBUG,
            },
        },
    ],
    WHITENOISE_ROOT=normpath(join(BASE_DIR, 'public')),
)


def index(request):
    return render(request, 'index.html')


urlpatterns = (
    url(r'^$', index),
)


application = DjangoWhiteNoise(get_wsgi_application())


if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
