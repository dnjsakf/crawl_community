BASE_URL = 'http://localhost:4000'
CORS = {
    r'*': { 'origins': 'localhost:4000/*' }
}
SECRET_KEY = 'AikpYFXdJGtqd3NRVLDTvri2pOxpzi7vcaF4WFC9TBY='
JWT_SECRET_KEY = 'AikpYFXdJGtqd3NRVLDTvri2pOxpzi7vcaF4WFC9TBY='
SESSION_TYPE = 'filesystem'

SESSION_COOKIE_HTTPONLY = True
REMEMBER_COOKIE_HTTPONLY = True