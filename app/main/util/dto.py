from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class WatchDto:
    api = Namespace('watch', description='watch related operations')
    watch = api.model('watch', {
        'watcher_id': fields.String(required=False, description='watcher Identifier'),
        'watched_id': fields.String(required=False, description='watched Identifier'),
    })


class FirebaseDto:
    api = Namespace('firebase', description='firebase related operations')
    firebase = api.model('firebase', {
        'token': fields.String(required=True, description='firebase token'),
    })