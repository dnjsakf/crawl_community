import jwt
import json

from app import app
from flask import jsonify, request, make_response
from functools import wraps
from datetime import datetime, timedelta
from app.utils.exceptions.AuthException import AuthException

class AuthDecorator(object):
  @staticmethod
  def isRole(session=None):
    def wrapper( func ):
      @wraps( func )
      def loggedWrapper(*args, **kwargs):
        app.logger.info( session )
        user = session['user'] if session and 'user' in session else None

        app.logger.info(f'user={ user }')

        if user:
          return {'success': False, 'user': user}
        else:
          return func(*args, **kwargs)
      return loggedWrapper
    return wrapper


  @staticmethod
  def token_requred( func ):
    @wraps( func )
    def wrapper(*args, **kwargs):
      jwt_secret_key = app.config['JWT_SECRET_KEY']
      token = request.cookies.get('access_token')
      
      user = None

      if token:
        try:
          decoded_token = jwt.decode(token, jwt_secret_key, algorithm='HS256')
        except Exception as e :
          raise AuthException("유효하지않은 Token 입니다.", 400)
        user = decoded_token['user']

      return func(user=user, *args, **kwargs)
    return wrapper


  @staticmethod
  def create_user_token( func ):
    @wraps( func )
    def wrapper(*args, **kwargs):
      response, status_code = func(*args, **kwargs)
      data = json.loads(response.get_data().decode('utf-8'))
      resp = make_response(data)

      if status_code == 200:
        jwt_secret_key = app.config['JWT_SECRET_KEY']
        payload = {
            "sub": "localhost:3000"
            , "iss": "heo_api"
            , "exp": int(datetime.timestamp(datetime.utcnow()+timedelta(hours=24)))
            , 'user': data['user']
        }
        token = jwt.encode(payload, jwt_secret_key, algorithm='HS256').decode('utf-8')

        resp.set_cookie('access_token', value=token, httponly=True)
      return resp, status_code

    return wrapper