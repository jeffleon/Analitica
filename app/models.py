from app import db
# from passlib.hash import pbkdf2_sha256 as sha256
import bcrypt

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role')

#     def __repr__(self):
#         return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, default="")
    password = db.Column(db.String(120), nullable=False , default="")
    name = db.Column(db.String(120), unique=True, default="")
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

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
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode("utf-8"), salt)

    """
    Verify hash and password
    """
    @staticmethod
    def verify_hash(password, hash_):
        return bcrypt.checkpw(password.encode("utf-8"), hash_.encode("utf-8"))

    def __repr__(self):
        return self.email