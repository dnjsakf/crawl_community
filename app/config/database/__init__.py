import app.config.database.mongodb as conf

URL = f'mongodb://{conf.USERNAME}:{conf.PASSWORD}@{conf.HOST}/{conf.DATABASE}?{conf.OPTIONS}'