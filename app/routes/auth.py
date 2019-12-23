import json

from app import app
from flask import Blueprint, jsonify, request, make_response, Response

from app.database.pipelines import AuthPipeline
from app.utils.decorators import AuthDecorator as auth

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

@bp_auth.route('/signin', methods=['POST'])
@auth.create_jwt_token
def authSignIn():
  secret_key = app.secret_key

  userinfo = request.json['userinfo']
  user = AuthPipeline(app.config['database']).checkSignIn( userinfo, secret_key )
  data = {
    'success': True
    , 'user': user
  }

  return jsonify(data), 200


@bp_auth.route('/signup', methods=['POST'])
def authSignUp():
  secret_key = app.secret_key

  userinfo = request.json['userinfo']
  result = AuthPipeline(app.config['database']).insertUser( userinfo, secret_key )
  data = {
    'success': True
    , 'user': { '_id': result }
  }
  return jsonify(data), 200

@bp_auth.route('/signout', methods=['POST'])
def authSignOut():
  resp = make_response({'success': True})
  resp.set_cookie('access_token', expires=0)
  return resp, 200

@bp_auth.route('/signchk', methods=['GET', 'POST'])
@auth.token_requred
def authSignCheck( data=None ):
  userId = data['_id']

  user = AuthPipeline(app.config['database']).selectUserInfo( userId )

  data = {
    'success': data is not None
    , 'user': user
  }
  return jsonify(data), 200


@bp_auth.route('/refresh', methods=['POST'])
@auth.refresh_jwt_token
def refreshJwtToken():
  return jsonify({}), 200