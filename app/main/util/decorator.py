from functools import wraps
from flask import request

from app.main.service.auth_helper import Auth


# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#
#         data, status = Auth.get_logged_in_user(request)
#         token = data.get('data')
#
#         if not token:
#             return data, status
#
#         #token_id = token.get('token_id')
#         return f(token_id, *args, **kwargs)
#
#     return decorated

