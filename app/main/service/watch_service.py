from app.main import db
from app.main.model.watch import Watch
from app.main.model.user import User
from sqlalchemy import and_
from flask import jsonify


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def get_all_watch(public_id):
    already_watched = db.session.query(Watch.watched_id).filter(Watch.watcher_id == public_id).subquery()
    all_users = db.session.query(User).filter(and_(User.public_id != public_id, ~User.public_id.in_(already_watched))).all()
    response = jsonify([i.serialize for i in all_users])
    response.status_code = 200
    return response


def remove_watch(watcher_id, watched_id):
    Watch.query.filter_by(watcher_id=watcher_id, watched_id=watched_id).delete()
    Watch.query.filter_by(watcher_id=watched_id, watched_id=watcher_id).delete()
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'watch deleted'
    }
    return response_object, 201


def save_new_watch(watcher_id, watched_id):
    watch = Watch.query.filter_by(watcher_id=watcher_id, watched_id=watched_id).first()
    if not watch:
        new_watch = Watch(
            watcher_id=watcher_id,
            watched_id=watched_id,
            pending=True
        )
        save_changes(new_watch)
        response_object = {
            'status': 'success',
            'message': 'Watch added'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Watch exists',
        }
        return response_object, 408


def approve_watch(watcher_id, watched_id):
    Watch.query.filter_by(watcher_id=watcher_id, watched_id=watched_id).update({"pending": False})
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Watch approved'
    }
    return response_object, 201


def get_all_watched(public_id):
    watched = db.session.query(Watch.pending, User.public_id, User.username, User.email).filter(Watch.watcher_id == public_id).join(User, Watch.watched_id == User.public_id).all()
    response = jsonify([i._asdict() for i in watched])
    response.status_code = 200
    return response


def get_all_watcher(public_id):
    watcher = db.session.query(Watch.pending, User.public_id, User.username, User.email).filter(Watch.watched_id == public_id).join(User, Watch.watcher_id == User.public_id).all()
    response = jsonify([i._asdict() for i in watcher])
    response.status_code = 200
    return response


