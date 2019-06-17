import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '2$+syn4q6bca)s48r)sdrilz-j8m+fyu6y86wn(knb%o%v_b=n'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'social_django',
]
AUTHENTICATION_BACKENDS = [
        'social_core.backends.linkedin.LinkedinOAuth2',
        'social_core.backends.instagram.InstagramOAuth2',
        'social_core.backends.facebook.FacebookOAuth2',  #facebook not working
        'django.contrib.auth.backends.ModelBackend',
    ]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'SocialAuth.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', 
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]
WSGI_APPLICATION = 'SocialAuth.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

LOGIN_URL = 'http://127.0.0.1:8000/login/'
LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/home/'
#LOGOUT_URL = 'http://127.0.0.1:8000/logout/'
#LOGOUT_REDIRECT_URL = 'http://127.0.0.1:8000/home/'

SOCIAL_AUTH_INSTAGRAM_KEY = ''      #Client ID
SOCIAL_AUTH_INSTAGRAM_SECRET = ''  #Client SECRET
SOCIAL_AUTH_INSTAGRAM_EXTRA_DATA = [         ('user', 'user'),]
SOCIAL_AUTH_INSTAGRAM_REDIRECT_URL = 'http://127.0.0.1:8000/social-auth/complete/instagram/',
    

SOCIAL_AUTH_FACEBOOK_KEY = ''          # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = ''      # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link'] 
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       
      'fields': 'id, name, email, picture.type(large), link'
    }
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 
        ('name', 'name'),
        ('email', 'email'),
        ('picture', 'picture'),
        ('link', 'profile_url'),
    ]    

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = ''        #Client ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = ''  #Client Secret
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'formatted-name', 'public-profile-url', 'picture-url']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
        ('id', 'id'),
        ('formattedName', 'name'),
        ('emailAddress', 'email_address'),
        ('pictureUrl', 'picture_url'),
        ('publicProfileUrl', 'profile_url'),
    ]    
