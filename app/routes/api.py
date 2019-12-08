from flask import jsonify, request
from app import app

from tasks import crawl

@app.route('/api', methods=[ 'GET', 'POST' ])
def apiTask():

    crawl.test.delay()

    return 'test'

@app.route('/api/ygosu', methods=[ 'GET', 'POST' ])
def apiYgosu():

    task = crawl.runCommunitySpider.delay(cate='adultpic', page=1)

    return jsonify({"type":"CommunitySpider", "task.id":task.id})

@app.route('/api/media', methods=[ 'GET', 'POST' ])
def apiMedia():

    task = crawl.runMeidaSpider.delay()

    return jsonify({"type":"MediaSpider", "task.id":task.id})