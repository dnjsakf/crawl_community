from app import app
from app.utils.crypt.AESCipher import AESCipher
from app.utils.exceptions.AuthException import AuthException

from bson.objectid import ObjectId

class AuthPipeline(object):

  client = None

  @classmethod
  def __init__(cls, client):
    cls.client = client

  @classmethod
  def insertUser( cls, userinfo ):
    exists = cls.client['test']['users'].find_one({"email": userinfo['email']})

    if not exists:
      userinfo['password'] = AESCipher(app.secret_key).encrypt_str(userinfo['password'])

      result = cls.client['test']['users'].insert_one( userinfo )

      if result:
        return str(result.inserted_id)
      else:
        raise AuthException('존재하지 않는 이메일입니다.', 400)
    raise AuthException('이미 가입된 이메일입니다.', 400)


  @classmethod
  def selectUser( cls, userinfo ):
    result = cls.client['test']['users'].find_one({'email': userinfo['email']})

    if result:
      result['_id'] = str( result['_id'] )
      result = dict( result )

      if AESCipher(app.secret_key).compare(userinfo['password'], result['password']):
        del result['password']
        return result
      else:
        raise AuthException('패스워드가 일치하지 않습니다.', 400)
    raise AuthException('사용자를 찾을 수 없습니다.', 400)

