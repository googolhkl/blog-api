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
