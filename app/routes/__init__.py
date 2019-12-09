from flask import render_template
from app import app
from app.routes.api import bp_api
from app.routes.auth import bp_auth
from flask_cors import cross_origin

app.register_blueprint(bp_api, url_prefix='/api')
app.register_blueprint(bp_auth, url_prefix='/auth')

@app.route('/', methods=['GET', 'POST'])
def main_index():
    return render_template('index.html')

@app.after_request
@cross_origin(supports_credentials=True)
def after(response):
    return response