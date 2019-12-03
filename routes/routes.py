from flask import jsonify

from extension import app


@app.route('/')
def hello():
    return 'lks'