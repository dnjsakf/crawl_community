from app import app
from flask import jsonify
from flask_cors import cross_origin

class AuthException(Exception):
  def __init__(self, message, status_code=400, payload=None):
    super(AuthException, self).__init__()
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

@app.errorhandler(AuthException)
def AuthHandler( error ):
  app.logger.error( error.to_dict() )
  return jsonify(error.to_dict()), error.status_code