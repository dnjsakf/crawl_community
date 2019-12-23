from app import app
from flask import jsonify

class CntsException(Exception):
  def __init__(self, message, status_code=400, payload=None):
    super(CntsException, self).__init__()
    self.message = message
    self.status_code = status_code
    self.payload = payload

  def __str__(self):
    return '[{status_code}] {message}'.format(status_code=self.status_code, message=self.message)
  
  def to_dict(self):
    return {
      "status_code": self.status_code
      , "message": self.message
      , "payload": self.payload
    }

@app.errorhandler(CntsException)
def AuthHandler( error ):
  app.logger.error( error )
  return jsonify(error.to_dict()), error.status_code