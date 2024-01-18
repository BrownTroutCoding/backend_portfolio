from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Import routes after the app has been defined
from routes import *

# this 'application factory' fixed the flask run error I was getting. Keeping for future use
# from flask import Flask
# def create_app():
#     app = Flask(__name__)
#     @app.route('/')
#     def hello_world():
#         return 'Hello, World!'
#     return app
# app = create_app()