from datetime import datetime, timedelta

BASE_URL = 'http://localhost:4000'
CORS = {
    r'*': { 'origins': 'localhost:4000/*' }
}

SECRET_KEY = 'AikpYFXdJGtqd3NRVLDTvri2pOxpzi7vcaF4WFC9TBY='

SESSION_COOKIE_HTTPONLY = True
REMEMBER_COOKIE_HTTPONLY = True

REDIS_HOST = 'your redis server'
REDIS_PORT = 6379
REDIS_DB = '0'
REDIS_TIMEOUT = 1

JWT_SECRET_KEY = 'AikpYFXdJGtqd3NRVLDTvri2pOxpzi7vcaF4WFC9TBY='
JWT_ACCESS_TOKEN_EXPIRE = timedelta( minutes=60 )
JWT_REFRESH_TOKEN_EXPIRE = timedelta( hours=24 )
JWT_EXPIRE_DELAY = timedelta( minutes=5 )