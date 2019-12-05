import os
import dotenv
from flask import Flask
from flask_cors import CORS

app = Flask(__name__, root_path='', static_folder='/static', template_folder='app/templates')

def createApp(env='dev'):

    from app.routes import route_api

    envConfFile = os.path.join(os.path.dirname(__file__), 'config/env', '.env')
    envConf = dotenv.load_dotenv( dotenv_path=envConfFile )
    app.config.from_object( envConf )

    pyConfFile = os.path.join(os.path.dirname(__file__), 'config/env', f'env.{env}.py')
    app.config.from_pyfile( pyConfFile )

    celeryConfFile = os.path.join('tasks', f'celeryconfig.py')
    app.config.from_pyfile( celeryConfFile )

    print( app.config )

    if 'CORS' in app.config:
        CORS( app=app, resources=app.config['CORS'] )

    return app