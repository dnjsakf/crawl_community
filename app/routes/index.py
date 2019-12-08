from app import app
from flask import jsonify, render_template, make_response

@app.route('/', methods=['GET', 'POST'])
def main_index():
    return render_template('index.html')