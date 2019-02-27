from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api()

@classmethod
def reset(cls):
    # cls.db = SQLAlchemy()
    cls.api = Api()