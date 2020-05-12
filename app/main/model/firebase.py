from .. import db


class Firebase(db.Model):
    """ Firebase Model for storing firebase token related details """
    __tablename__ = "firebase"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100))
    token = db.Column(db.String(500))

    @property
    def serialize(self):
        return {
            'token': self.token
        }

    def __repr__(self):
        return "<Firebase '{}'>".format(self.public_id)
