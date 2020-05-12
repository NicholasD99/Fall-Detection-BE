import sys

from flask import request
from flask_restplus import Resource

from ..util.dto import FirebaseDto
from ..service.firebase_service import add_token, remove_token, list_all, get_help
from app.main.service.auth_helper import Auth

api = FirebaseDto.api
_firebase = FirebaseDto.firebase


@api.route('/')
class ListFirebase(Resource):
    @api.doc('list_of_firebase_tokens')
    def get(self):
        """List all firebase tokens"""
        list_all()


@api.route('/add/')
class AddFirebase(Resource):
    @api.response(201, 'token successfully added')
    @api.doc('Add a token')
    @api.expect(_firebase, validate=True)
    def post(self):
        """Adds a new firebase token for the user"""
        data, status = Auth.get_logged_in_user(request)
        public_id = data['data']['id']
        req_data = request.json
        return add_token(data=req_data, public_id=public_id)


@api.route('/remove/')
class RemoveFirebase(Resource):
    @api.response(201, 'token successfully removed')
    @api.doc('Remove a token')
    @api.expect(_firebase, validate=True)
    def post(self):
        """Removes a firebase token for the user"""
        data, status = Auth.get_logged_in_user(request)
        public_id = data['data']['id']
        req_data = request.json
        return remove_token(data=req_data, public_id=public_id)


@api.route('/help/')
class AddFirebase(Resource):
    @api.response(201, 'notified')
    @api.doc('Notifies')
    def get(self):
        """Notifies"""
        data, status = Auth.get_logged_in_user(request)
        public_id = data['data']['id']
        return get_help(public_id=public_id)
