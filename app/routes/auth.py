from app import app
from flask import Flask, jsonify, request

from app.utils.database.pipelines.AuthPipeline import AuthPipeline

@app.route('/auth/signin', methods=['POST'])
def authSignIn():
  assert 'userinfo' in request.json

  data = {}

  userinfo = request.json['userinfo']

  user, error = AuthPipeline(app.config['database']).selectUser( userinfo )
  if error:
    app.logger.info( error() )
    data['success'] = False
    data['user'] = {}
    
  else:
    data['success'] = True
    data['user'] = user

  return jsonify( data )

@app.route('/auth/signup', methods=['POST'])
def authSignUp():
  assert 'userinfo' in request.json

  data = {}

  userinfo = request.json['userinfo']

  result, error = AuthPipeline(app.config['database']).insertUser( userinfo )
  if error:
    app.logger.info( error() )
    data['success'] = False
    data['user'] = {}
  else:
    data['success'] = True
    data['user'] = { '_id': result }

  return jsonify( data )