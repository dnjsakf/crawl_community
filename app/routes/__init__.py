from flask import render_template
from app import app
from app.routes.api import bp_api
from app.routes.auth import bp_auth
from app.routes.cnts import bp_communities, bp_users
from flask_cors import cross_origin

app.register_blueprint(bp_api, url_prefix='/api')
app.register_blueprint(bp_auth, url_prefix='/auth')
app.register_blueprint(bp_communities, url_prefix='/cnts/communities')
app.register_blueprint(bp_users, url_prefix='/cnts/users')

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')


@app.after_request
@cross_origin(supports_credentials=True)
def after(response):
  return response