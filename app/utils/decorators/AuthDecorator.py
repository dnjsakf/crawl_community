import time
import jwt
import json
import uuid
import redis

from app import app
from flask import jsonify, request, make_response
from functools import wraps
from datetime import datetime, timedelta

from werkzeug.exceptions import Unauthorized
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from app.exceptions import AuthException

class AuthDecorator(object):
  @staticmethod
  def token_requred( func ):
    @wraps( func )
    def wrapper(*args, **kwargs):
      data = None
      token = request.cookies.get('access_token')
      if token is not None:
        try:
          jwt_secret_key = app.config['JWT_SECRET_KEY']
          jwt_leeway = app.config['JWT_EXPIRE_DELAY']

          decoded_payload = decode_token(token, True)

          now = datetime.now()
          expire = datetime.fromtimestamp(decoded_payload['exp'])

          if ( now >= expire ):
            pass
            raise AuthException("Token이 곧 만료됩니다.", 401, {'refresh': True})
          else:
            data = decoded_payload['data']
        except ExpiredSignatureError as e:
          raise AuthException("만료된 Token 입니다.", 401, {'error': str(e)})
        except InvalidTokenError as e :
          raise AuthException("유효하지않은 Token 입니다.", 401, {'error': str(e)})
        except AuthException as e:
          raise e
        except Exception as e:
          raise AuthException("인증 오류가 발생하였습니다.", 401, {'error': str(e)})
      else:
        raise AuthException("Token이 존재하지 않습니다.", 401)
      return func(data=data, *args, **kwargs)
    return wrapper


  @staticmethod
  def create_jwt_token( func ):
    @wraps( func )
    def wrapper(*args, **kwargs):
      response, status_code = func(*args, **kwargs)
      data = json.loads(response.get_data().decode('utf-8'))

      if status_code == 200:
        refresh_expire = datetime.utcnow() + app.config['JWT_REFRESH_TOKEN_EXPIRE']
        access_expire = datetime.utcnow() + app.config['JWT_ACCESS_TOKEN_EXPIRE']
        cookie_expire = access_expire + app.config['JWT_EXPIRE_DELAY']

        access_token, access_id = create_token(data=data['user'], expire=access_expire)
        refresh_token, refresh_id = create_token(data=data['user'], expire=refresh_expire)

        try:
          client = connect_redis()
          client.set(refresh_id, refresh_token)

        # except (redis.ConnectionError, redis.TimeoutError, redis.BusyLoadingError) as e:
        #   raise Unauthorized(description=e)
        except Exception as e:
          raise Unauthorized(description=str(e))

        data['token'] = refresh_id

        app.logger.info(f'data => {data}')

        response = make_response( data )
        response.set_cookie('access_token', value=access_token, httponly=True, expires=cookie_expire)

        return response, status_code
      else:
        return response, status_code

    return wrapper


  @staticmethod
  def refresh_jwt_token( func ):
    @wraps(func)
    def wrapper(*args, **kwargs):
      response, status_code = func(*args, **kwargs)

      jwt_secret_key = app.config['JWT_SECRET_KEY']
      access_expire = datetime.utcnow() + app.config['JWT_ACCESS_TOKEN_EXPIRE']
      cookie_expire = access_expire + app.config['JWT_EXPIRE_DELAY']

      refresh_id = request.json.get('token')
        
      try:
        client = connect_redis()
        refresh_token = client.get(refresh_id)

        decoded_payload = decode_token(refresh_token, leeway=False)
        access_token, access_id = create_token(data=decoded_payload['data'], expire=access_expire)

        response.set_cookie('access_token', value=access_token, httponly=True, expires=cookie_expire)

      except Exception as e:
        raise Unauthorized(description=e)

      return response, status_code
    return wrapper


def create_token(data=None, expire=datetime.utcnow()+timedelta(hours=24)):
  jwt_secret_key = app.config['JWT_SECRET_KEY']

  token_id = str(uuid.uuid4())
  payload = {
      'sub': 'localhost:3000'
      , 'iss': 'heo_api'
      , 'exp': expire
      , 'data': data
      , 'jti': token_id
  }
  token = jwt.encode(payload, jwt_secret_key, algorithm='HS256').decode('utf-8')

  return token, token_id


def decode_token(token=None, leeway=False):
  jwt_secret_key = app.config['JWT_SECRET_KEY']
  jwt_leeway = app.config['JWT_EXPIRE_DELAY'] if leeway else 0
  
  try:
    decoded_token = jwt.decode(token, jwt_secret_key, leeway=jwt_leeway, algorithm='HS256')
    return decoded_token
  except Exception as e:
    raise e


def connect_redis():
  redis_host = app.config['REDIS_HOST']
  redis_port = app.config['REDIS_PORT']
  redis_db = app.config['REDIS_DB']
  redis_timeout = app.config['REDIS_TIMEOUT']

  client = None
  try:
    client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, socket_timeout=redis_timeout)
    app.logger.info( f'ping { client.ping() }' )
  except Exception as e:
    raise e

  return client