import app.config.database.mongo as mongo

MONGO_URL = f'{mongo.MODULE}://{mongo.USERNAME}:{mongo.PASSWORD}@{mongo.HOST}/{mongo.DATABASE}?{mongo.OPTIONS}'