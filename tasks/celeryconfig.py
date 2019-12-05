CELERY_IMPORTS = ("tasks.crawl",)
CELERY_RESULT_BACKED='amqp://guest:guest@localhost:5672/'
BROKER_URL='amqp://guest:guest@localhost:5672/'

CELERYD_MAX_TASKS_PER_CHILD = 1