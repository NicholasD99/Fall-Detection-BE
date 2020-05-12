from app.main import db
from app.main.model.firebase import Firebase
from app.main.model.watch import Watch
from flask import jsonify
from firebase_admin import messaging
from pyfcm import FCMNotification



def save_changes(data):
    db.session.add(data)
    db.session.commit()


def list_all():
    return Firebase.query.all()


def add_token(data, public_id):
    firebase = Firebase.query.filter_by(public_id=public_id, token=data['token']).first()
    if not firebase:
        new_watch = Firebase(
            public_id=public_id,
            token=data['token']
        )
        save_changes(new_watch)
        response_object = {
            'status': 'success',
            'mesage': 'Firebase token added',
            'token': data['token'],
            'public_id': public_id,
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'success',
            'message': 'Firebase token exists',
        }
        return response_object, 202


def remove_token(data, public_id):
    firebase = Firebase.query.filter_by(public_id=public_id, token=data['token']).first()
    if firebase:
        Firebase.query.filter_by(public_id=public_id, token=data['token']).delete()
        db.session.commit()
        response_object = {
            'status': 'success',
            'mesage': 'Firebase token deleted'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'success',
            'message': 'Firebase token does not exist'
        }
        return response_object, 202


def get_help(public_id):
    watch = Watch.query.filter_by(watched_id=public_id, pending=False).all()
    watchers = db.session.query(Watch.watcher_id).filter(Watch.watched_id == public_id).subquery()
    all_tokens = db.session.query(Firebase).filter(Firebase.public_id.in_(watchers)).all()
    tokens = []
    for i in all_tokens:
        tokens.append(i.serialize['token'])
    message_title = "Someone Fell"
    message_body = "Unfortunate"
    push_service = FCMNotification(api_key="")
    result = push_service.notify_multiple_devices(registration_ids=tokens, message_title=message_title, message_body=message_body)
    response_object = {
        'status': 'success',
        'message': 'sent'
    }
    return response_object, 201
