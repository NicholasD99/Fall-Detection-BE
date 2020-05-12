from .. import db


class Watch(db.Model):
    """ Watch Model for storing watching related details """
    __tablename__ = "watch"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    watched_id = db.Column(db.String(100))
    watcher_id = db.Column(db.String(100))
    pending = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return "<Watch '{}'>".format(self.id)
