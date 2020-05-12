# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.watch_controller import api as watch_ns
from .main.controller.firebase_controller import api as firebase_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Fall-Detection API',
          version='1.0',
          description='for users, subscriptions, and watching'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(watch_ns)
api.add_namespace(firebase_ns)
