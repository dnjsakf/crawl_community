from app import app
from flask import jsonify

from app.exceptions.AuthException import AuthException
from app.exceptions.CntsException import CntsException

@app.errorhandler( Exception )
def ExceptionHandler( error ):
  return jsonify({
    "status_code": 500
    , "message": error
    , "payload": None
  }), 500