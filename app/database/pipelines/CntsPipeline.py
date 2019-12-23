from app.utils.crypt import AESCipher
from app.exceptions import CntsException

from bson.objectid import ObjectId

class CntsPipeline(object):

  client = None

  @classmethod
  def __init__(cls, client):
    cls.client = client

  @classmethod
  def selectCommunities( cls ):
    result = list(cls.client['test']['community_info'].aggregate([
      { 
        '$addFields': { 
          '_id': { '$toString': '$_id' } 
        } 
      }
    ]))

    if result and len(result) > 0:
      return result

    raise CntsException('콘텐츠가 없습니다.', 201)
      

