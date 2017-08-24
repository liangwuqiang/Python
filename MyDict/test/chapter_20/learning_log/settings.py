"""
Django settings for learning_log project.
# ## Django learning_log项目设置。

Generated by 'django-admin startproject' using Django 1.8.4.
# ## 使用Django 1.8.4由“django-admin startproject”。

For more information on this file, see
# ## 关于这个文件的更多信息,请参阅
https://docs.djangoproject.com/en/1.8/topics/settings/
# ## https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
# ## 设置的完整列表和他们的价值观,明白了
https://docs.djangoproject.com/en/1.8/ref/settings/
# ## https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# ## 在项目构建路径:os.path。加入(BASE_DIR…)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# ## 快速启动开发设置,不适合生产
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
# ## 参见https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# ## 安全警告:生产中使用的密钥保密!
SECRET_KEY = 'make_your_own_secret_key'

# SECURITY WARNING: don't run with debug turned on in production!
# ## 安全警告:不要在生产运行与调试打开!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition
# ## 应用程序定义

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    # ## 第三方应用程序
    'bootstrap3',
    
    # My apps
    # ## 我的应用程序
    'learning_logs',
    'users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'learning_log.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'learning_log/templates')],
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

WSGI_APPLICATION = 'learning_log.wsgi.application'


# Database
# ## 数据库
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# ## https://docs.djangoproject.com/en/1.8/ref/settings/数据库

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# ## 国际化
# https://docs.djangoproject.com/en/1.8/topics/i18n/
# ## https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# ## 静态文件(CSS、JavaScript、图像)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# ## https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# My settings
# ## 我的设置
LOGIN_URL = '/users/login/'

# Settings for django-bootstrap3
# ## 设置django-bootstrap3
BOOTSTRAP3 = {
    'include_jquery': True,
    }

# Heroku settings
# ## Heroku的设置
if os.getcwd() == '/app':
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default='postgres://localhost')
    }
    
    # Honor the 'X-Forwarded-Proto' header for request.is_secure().
    # ## 尊重“X-Forwarded-Proto”头request.is_secure()。
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
    # Only allow heroku to host the project.
    # ## 只允许heroku主办项目。
    ALLOWED_HOSTS = ['learning-log-final.herokuapp.com']
    DEBUG = False

    # Static asset configuration
    # ## 静态资产配置
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
