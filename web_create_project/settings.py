"""
Django settings for web_create_project project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
# 9/16 import library
import django_heroku
from decouple import config
import whitenoise
import dj_database_url
# 9/16 import library

import os

"""9/25新增會員登入頁面成功跳轉畫面"""
LOGIN_REDIRECT_URL = '/login'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
"""9/25新增會員登入頁面成功跳轉畫面"""

"""9/27 新增 google API第三方 為 localhost 使用"""
AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',  # 預設
        'social_core.backends.google.GoogleOAuth2',   # 新增於9/27
        'social_core.backends.github.GithubOAuth2',   # 新增於9/27
        # 'social_core.backends.facebook.FacebookOAuth2',  # 新增於9/28
        'social_core.backends.instagram.InstagramOAuth2',  #新增於9/28
]
SOCIAL_AUTH_URL_NAMESPACE = 'social'
# localhost key secret
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '191042244574-rcvbcumjt3tmhtcetnealn89co1fmbli.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ZNb2y_niK1mYkXAg38Wsnnut'
# SOCIAL_AUTH_GITHUB_KEY = 'b8c658e7ee2d2bc9dc03'
# SOCIAL_AUTH_GITHUB_SECRET = '83be6a407ca7b1051e62384c2fbe4809648b279b'


# heroku key secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '191042244574-3fsaenguf469lhde81a5493usk27hrjo.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '9SrlkIlZ2jztLbeRgCjTveTE'
SOCIAL_AUTH_GITHUB_KEY = '882927535ceb6c029118'
SOCIAL_AUTH_GITHUB_SECRET = 'cd014409817cd5039c4a175fa019c9a41246b074'
# SOCIAL_AUTH_FACEBOOK_KEY = '484749135713335' # 與 local端設定一樣
# SOCIAL_AUTH_FACEBOOK_SECRET = '9a65d47f0f800cfe8258705db972aa1e' # 與 local端設定一樣
SOCIAL_AUTH_INSTAGRAM_KEY = '766b10862faf47c3b0f34c6476a62047'  # 與 local端設定一樣
SOCIAL_AUTH_INSTAGRAM_SECRET = 'd4be61d6dc6344e5974d5e94bded3ec1'  # 與 local端設定一樣
"""9/27 新增 google API第三方"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY') # 9/17新增
# SECRET_KEY = '%4qakn%#z8ty4v3r2a4404+_abswk65kjgwrd2n@sdb6lr^3^p' # 9/17剪下至.env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  #真正上線部署時會設定為False 改為False 9/15

# ALLOWED_HOSTS = []
"""9/27 修改hosts運行第三方"""
ALLOWED_HOSTS = ['jamie.com', ]
"""9/27 修改hosts運行第三方"""


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  #新增的app
    'to_do',  #新增於0912
    'login',  #新增於0925
    'social_django',  # 新增於0927
]
#     'mysqlfile', # 2019/09/08 新增mysql
# 9/15新增heroku whitenoise 處理 static 文件
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


ROOT_URLCONF = 'web_create_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #加上templates路徑 自己加的
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

WSGI_APPLICATION = 'web_create_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
'''sqlite3'''
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
'''09/08 改為 mysql，因為上船雲端，所以db換成 postgresql '''
"""09/25 開發 mysql login 使用 下午四點換過去postgresql """
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':'login',  # 使用數據庫名字 數據需先手動創建
#         'USER':'b10130402',
#         'PASSWORD':'hjkl4660',
#         'HOST':'localhost',  # 指定mysql數據庫所在ip位址'127.0.0.1'
#         'PORT':'3306',
#         'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",},
#     }
# }
"""9/19 更該為postgresql"""
"""9/25 重新啟用 postgresql"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql.psycopg2',
    }
}
### 其 url 24hrs 會更換 ，使用此式 local & heroku 資料庫共通
DATABASES['default'] = dj_database_url.config(default="postgres://dmpdzkbcivfuhy:b2c275dfba4397ed9159d74d22e3727ad122bddc95937cbe6e9560dd4d5dcc68@ec2-174-129-227-128.compute-1.amazonaws.com:5432/da29d5835f52dv")
db_from_env = dj_database_url.config(conn_max_age= 600)
DATABASES['default'].update(db_from_env)
"""9/19 更該為postgresql"""
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

LANGUAGE_CODE = 'zh-Hant' #使用中文

TIME_ZONE = 'Asia/Taipei' #使用時區

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ #加入static路徑
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 9/17 新增
django_heroku.settings(locals())