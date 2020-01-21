from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)


@app.route('/')
def show_user_profile(username):
    return "just main page"

@app.route('/take')
def show_user_profile(username):
    return "sth from firebase"

