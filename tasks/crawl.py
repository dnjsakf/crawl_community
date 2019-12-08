import time

from communities.spiders import MediaSpider, YgosuSpider

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from scrapy import signals

from twisted.internet import reactor

from celery import Celery, task
from celery.utils.log import get_task_logger

app = Celery(__name__)
logger = get_task_logger(__name__)

class SpiderRunner(CrawlerRunner):
    def __init__(self, spider):
        settings = get_project_settings()
        super(SpiderRunner, self).__init__( settings )
        self.spider = spider

    def run(self, *args, **kwargs):
        self.crawl( self.spider, *args, **kwargs )
        deferred = self.join()
        deferred.addBoth(lambda _: reactor.stop())
        reactor.callFromThread(lambda duration: time.sleep(duration), 5)
        reactor.run()

@app.task(ignore_result=True)
def runCommunitySpider(*args, **kwargs):
    print( 'runCommunitySpider' )
    runner = SpiderRunner( YgosuSpider )
    runner.run(*args, **kwargs)

@app.task(ignore_result=True)
def runMeidaSpider(*args, **kwargs):
    print( 'runMeidaSpider' )
    runner = SpiderRunner( MediaSpider )
    runner.run(*args, **kwargs)
