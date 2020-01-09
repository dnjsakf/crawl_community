from app import app
from flask import jsonify

from werkzeug.exceptions import HTTPException
from app.exceptions.AuthException import AuthException
from app.exceptions.CntsException import CntsException

@app.errorhandler( HTTPException )
def HttpExceptionHandler( error ):
  app.logger.info(f'[HTTPException] { error.code } { error.description }')
  return jsonify({
    "status_code": error.code
    , "message": error.description
    , "payload": None
  }), error.code

@app.errorhandler( Exception )
def ExceptionHandler( error ):
  app.logger.info(f'[Exception] 500 { str(error) }')
  return jsonify({
    "status_code": 500
    , "message": str(error)
    , "payload": None
  }), 500