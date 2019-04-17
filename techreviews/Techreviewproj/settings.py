INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'techapp',
]

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'techprojectdb',
        'USER' : 'postgres',
        'PASSWORD': 'P@ssw0rd1',
        'HOST' :'localhost',
        'PORT' :'',
    }
}
