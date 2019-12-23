import app

from app import app
from flask import Blueprint, jsonify, request, make_response, Response

from app.database.pipelines import CntsPipeline
from app.utils.decorators import AuthDecorator as auth

bp_communities = Blueprint('cnts/communities', __name__, url_prefix='/cnts/communities')

@bp_communities.route('/list', methods=['GET'])
@auth.token_requred
def getCommunities(data=None):
  communities = CntsPipeline(app.config['database']).selectCommunities()

  data = {
    'success': True
    , 'data': communities
  }

  return jsonify(data), 200
  