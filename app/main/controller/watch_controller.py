import sys

from flask import request
from flask_restplus import Resource


from ..util.dto import WatchDto
from ..service.watch_service import get_all_watcher, get_all_watched, save_new_watch, get_all_watch, remove_watch, approve_watch
from app.main.service.auth_helper import Auth

api = WatchDto.api
_watch = WatchDto.watch


@api.route('/')
class Watch(Resource):
    @api.doc('list_of_registered_users')
    def get(self):
        """List all registered users"""
        data, status = Auth.get_logged_in_user(request)
        public_id = data['data']['id']
        return get_all_watch(public_id=public_id)

    @api.response(201, 'Watch successfully created.')
    @api.doc('create a new watch')
    @api.expect(_watch, validate=True)
    def post(self):
        """Creates a new Watch """
        data, status = Auth.get_logged_in_user(request)
        public_id = data['data']['id']
        request_data = request.json
        return save_new_watch(watcher_id=public_id, watched_id=request_data['public_id'])


@api.route('/remove/')
class WatchRemove(Resource):
    @api.response(201, 'Watch successfully removed')
    @api.doc('removes an existing watch')
    @api.expect(_watch, validate=True)
    def post(self):
        """Removes a watch """
        data, status = Auth.get_logged_in_user(request)
        public_id = data['data']['id']
        request_data = request.json
        return remove_watch(watcher_id=public_id, watched_id=request_data['public_id'])


@api.route('/approve/')
class WatchApprove(Resource):
    @api.response(201, 'Watch successfully approved.')
    @api.doc('approve an existing watch')
    def post(self):
        """Approves a watch """
        data, status = Auth.get_logged_in_user(request)
        public_id = data['data']['id']
        request_data = request.json
        return approve_watch(watcher_id=request_data['public_id'], watched_id=public_id)


@api.route('/watching/')
class Watched(Resource):
    @api.doc('get all users watched by this user')
    def get(self):
        """get all users watched by this user"""
        data, status = Auth.get_logged_in_user(request)
        public_id = data['data']['id']
        return get_all_watched(public_id=public_id)


@api.route('/watchers/')
class Watcher(Resource):
    @api.doc('gets all users watching this user')
    def get(self):
        """gets all users watching this user"""
        data, status = Auth.get_logged_in_user(request)
        public_id = data['data']['id']
        # public_id = 'ce77397c-33f6-43a2-a8a2-035c1467cf60'
        return get_all_watcher(public_id=public_id)
