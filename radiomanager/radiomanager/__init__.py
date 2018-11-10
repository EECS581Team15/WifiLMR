"""
radiomanager
============

WifiLMR's backend server. Handles authentication, fleet management, and call
routing.
"""

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .api import setup_routing

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

setup_routing(api)