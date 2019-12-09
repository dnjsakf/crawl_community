import json
import jwt

from app import app
from flask import Blueprint, jsonify, request, make_response, Response

from app.utils.database.pipelines.AuthPipeline import AuthPipeline
from app.utils.decorators.AuthDecorator import AuthDecorator as auth

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

@bp_auth.route('/signin', methods=['POST'])
@auth.create_user_token
def authSignIn():
  userinfo = request.json['userinfo']
  user = AuthPipeline(app.config['database']).selectUser( userinfo )
  data = {
    'success': True
    , 'user': user
  }
  return jsonify(data), 200


@bp_auth.route('/signup', methods=['POST'])
def authSignUp():
  userinfo = request.json['userinfo']
  result = AuthPipeline(app.config['database']).insertUser( userinfo )
  data = {
    'success': True
    , 'user': { '_id': result }
  }
  return jsonify(data), 200


@bp_auth.route('/session', methods=['GET', 'POST'])
@auth.token_requred
def authSession( user=None ):
  data = {
    'success': user is not None
    , 'user': user
  }
  return jsonify(data), 200
