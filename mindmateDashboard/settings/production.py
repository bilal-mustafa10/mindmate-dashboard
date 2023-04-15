from .base import *

DEBUG = False

STATICFILES_STORAGE = 'mindmateDashboard.settings.storage_backends.StaticStorage'
DEFAULT_FILE_STORAGE = 'mindmateDashboard.settings.storage_backends.MediaStorage'


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'mindmate-dev'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    "ACL": "public-read",
    'CacheControl': 'max-age=86400',
}

STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'mindmateDashboard.settings.storage_backends.StaticStorage'

MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'mindmateDashboard.settings.storage_backends.MediaStorage'


try:
    from .local import *
except ImportError:
    pass
