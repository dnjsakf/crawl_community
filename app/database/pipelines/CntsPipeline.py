import re

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

  @classmethod
  def selectUsers( cls, **kwargs ):
    # Initialize
    pipeline = [{ 
      '$addFields': { 
        'username': { 
          '$concat': ['$lastName', '$firstName']
        },
        '_id': {
          '$toString': '$_id'
        }
      }
    }]

    # Conditions
    match = {
      '$match': dict()
    }

    if kwargs.get('email') is not None:
      match['$match']['email'] = {
        '$regex': re.compile( kwargs.get('email') )
      }

    if kwargs.get('username') is not None:
      match['$match']['username'] = {
        '$regex': re.compile( kwargs.get('username') )
      }

    if match['$match'] is not None and len( match['$match'] ) > 0 :
      pipeline.append( match )

    # Sorting
    if kwargs.get('sort') is not None:
      pipeline.append( { '$sort': kwargs.get('sort') } )
    else:
      pipeline.append( { '$sort': { 'regDate': -1 } } )

    # Pagination
    valid_page = kwargs.get('page') is not None and kwargs.get('page') != ''
    if valid_page:
      valid_rows = kwargs.get('rows') is not None and kwargs.get('rows') != ''
    
      page = int(kwargs.get('page'))
      rows = int(kwargs.get('rows')) if valid_rows else 10

      skip = ( page - 1 ) * rows
      limit = rows

      pipeline.append( { '$skip': skip } )
      pipeline.append( { '$limit': limit } )

    result = list(cls.client['test']['users'].aggregate( pipeline ))

    if result and len(result) > 0:
      return result

    raise CntsException('콘텐츠가 없습니다.', 201)
      
