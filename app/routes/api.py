from flask import jsonify, request
from app import app

from tasks import crawl

@app.route('/', methods=[ 'GET', 'POST' ])
def runTask():

    crawl.test.delay()

    return 'test'

@app.route('/ygosu', methods=[ 'GET', 'POST' ])
def runYgosu():

    task = crawl.runCommunitySpider.delay(cate='adultpic', page=1)

    return jsonify({"type":"CommunitySpider", "task.id":task.id})

@app.route('/media', methods=[ 'GET', 'POST' ])
def runMedia():

    task = crawl.runMeidaSpider.delay()

    return jsonify({"type":"MediaSpider", "task.id":task.id})