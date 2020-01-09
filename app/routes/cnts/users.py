import app

from app import app
from flask import Blueprint, jsonify, request, make_response, Response

from app.database.pipelines import CntsPipeline
from app.utils.decorators import AuthDecorator as auth

bp_users = Blueprint('cnts/users', __name__, url_prefix='/cnts/users')

@bp_users.route('/list', methods=['GET'])
@auth.token_requred
def getUsers(data=None):
  
  params = dict(request.args)

  users = CntsPipeline(app.config['database']).selectUsers( **params )
  data = {
    'success': True
    , 'data': users
  }

  return jsonify(data), 200
  