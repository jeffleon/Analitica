from app import db
from passlib.hash import pbkdf2_sha256 as sha256

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(120), nullable=False , default="")
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    """
    Save user details in Database
    """
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    """
    generate hash from password by encryption using sha256
    """
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    """
    Verify hash and password
    """
    @staticmethod
    def verify_hash(password, hash_):
        return sha256.verify(password, hash_)

    def __repr__(self):
        return self.username