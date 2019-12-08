from app import app
from app.utils.crypt.AESCipher import AESCipher
from app.utils.Exceptions.AuthException import AuthException, PasswordNotMatchedException, NotFoundUserException, AlreadyExistUserException

from bson.objectid import ObjectId

class AuthPipeline(object):

  client = None

  @classmethod
  def __init__(cls, client):
    cls.client = client


  @classmethod
  def insertUser( cls, userinfo ):
    secretKey = app.config['SECRET_KEY']

    exists = cls.client['test']['users'].find_one({"email": userinfo['email']})

    if not exists:
      userinfo['password'] = AESCipher(secretKey).encrypt_str(userinfo['password'])

      result = cls.client['test']['users'].insert_one( userinfo )

      if result:
        return ( str(result.inserted_id), None )
      else:
        return ( None, AuthException )
    else:
      return ( None, AlreadyExistUserException )


  @classmethod
  def selectUser( cls, userinfo ):
    secretKey = app.config['SECRET_KEY']

    result = cls.client['test']['users'].find_one({'email': userinfo['email']})

    if result:
      result['_id'] = str( result['_id'] )
      result = dict( result )

      if AESCipher(secretKey).compare(userinfo['password'], result['password']):
        return ( result, None )
      else:
        return ( None, PasswordNotMatchedException )
    return ( None, NotFoundUserException )


  @classmethod
  def selectUser2( cls, userinfo ):
    pipelines = []

    match = { "$match": {
        "email": userinfo["email"]
    } }
    addFields = {
      "$addFields": {
        "_id": { "$toString": "$_id" }
      }
    }
    project = {
      "$project": {
        "email": 1
        , "password": 1
        , "_id": 1
      }
    }
    limit = { "$limit": 1 }

    return list(cls.client['test']['users'].aggregate([ match, addFields, project, limit ]))
