from .common import *

# 실제 사용시 아래 내용을 적절하게 수정하고 파일명을 prod.py로 변경해야 합니다.
DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
	'NAME': 'postgres',
	'USER': '{DB_USER}',
	'PASSWORD': '{DB_USER_PASSWORD}',
	'HOST': '{HOST}',
	'PORT': '{PORT}',
    }
}

# S3 업로드
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID =  '{ACCESS_KEY_ID}'
AWS_SECRET_ACCESS_KEY = '{SECRET_ACCESS_KEY}'
AWS_STORAGE_BUCKET_NAME = '{BUCKET_NAME}'
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.ap-northeast-2.amazonaws.com'
