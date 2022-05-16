from app.extensions import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    isAdministrator = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %s>' % self.username