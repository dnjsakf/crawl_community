from flask import Blueprint, jsonify, request
from tasks import crawl

bp_api = Blueprint('api', __name__, url_prefix='/api')

@bp_api.route('/', methods=[ 'GET', 'POST' ])
def apiTask():

    crawl.test.delay()

    return 'test'

@bp_api.route('/ygosu', methods=[ 'GET', 'POST' ])
def apiYgosu():

    task = crawl.runCommunitySpider.delay(cate='adultpic', page=1)

    return jsonify({"type":"CommunitySpider", "task.id":task.id})

@bp_api.route('/media', methods=[ 'GET', 'POST' ])
def apiMedia():

    task = crawl.runMeidaSpider.delay()

    return jsonify({"type":"MediaSpider", "task.id":task.id})