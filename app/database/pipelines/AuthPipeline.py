from app.utils.crypt import AESCipher
from app.exceptions import AuthException

from bson.objectid import ObjectId

class AuthPipeline(object):

  client = None

  @classmethod
  def __init__(cls, client):
    cls.client = client

  @classmethod
  def insertUser( cls, userinfo, secret_key ):
    conditions = {
      "email": userinfo['email']
    }
    exists = cls.client['test']['users'].find_one( conditions )

    if not exists:
      userinfo['password'] = AESCipher( secret_key ).encrypt_str( userinfo['password'] )

      result = cls.client['test']['users'].insert_one( userinfo )

      if result:
        return str( result.inserted_id )
      else:
        raise AuthException('존재하지 않는 이메일입니다.', 400)
    raise AuthException('이미 가입된 이메일입니다.', 400)


  @classmethod
  def checkSignIn( cls, userinfo, secret_key ):
    result = list(cls.client['test']['users'].aggregate([
      { 
        '$match': { 
          'email': userinfo['email'] 
        }
      }, { 
        '$addFields': { 
          '_id': { '$toString': '$_id' } 
        } 
      }, { 
        '$limit': 1 
      }
    ]))

    if result and len(result) > 0:
      resultUser = dict( result[0] )

      if AESCipher( secret_key ).compare( userinfo['password'], resultUser['password'] ):
        del resultUser['password']
        return resultUser
      else:
        raise AuthException('패스워드가 일치하지 않습니다.', 400)
    raise AuthException('사용자를 찾을 수 없습니다.', 400)

  @classmethod
  def selectUserInfo( cls, userId ):
    result = list(cls.client['test']['users'].aggregate([
      { 
        '$match': { 
          '_id': ObjectId( userId )
        }
      }, {
        '$addFields': { 
          '_id': { '$toString': '$_id' } 
        } 
      }, {
        '$project': {
          'password': 0
        }
      }, { 
        '$limit': 1 
      }
    ]))

    if result and len(result) > 0:
      return dict( result[0] )
    raise AuthException('사용자를 찾을 수 없습니다.', 400)
      

