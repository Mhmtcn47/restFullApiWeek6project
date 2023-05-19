from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from secrets import token_urlsafe

from app import db,login

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model):
    user_id=  db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(60),unique=True)
    user_email =  db.Column(db.String(100),unique=True)
    user_password = db.Column(db.String(200))
    token =db.column(db.String(250),unique=True)
    date_created= db.Column(db.DateTime, default=datetime.utcnow)
    character= db.relationship('Post',backref='author', lazy=True)

    def __repr__(self):
        return f'User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self,password):
        return generate_password_hash(password)



class MarvelCharacters(db.Model):
    char_id = db.Column(db.Integer,primary_key=True)
    char_name = db.Column(db.String(60),unique=True)
    char_email = db.Column(db.String(100),unique=True)
    char_password = db.Column(db.String(200))
    token = db.column(db.String(250),unique=True)
    date_created=  db.Column(db.DateTime, default=datetime.utcnow)
    character  = db.relationship('Post', backref='author', lazy=True)


    def __repr__(self):
        return f'MarvelCharacters {self.body}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self,password):
        return generate_password_hash(password)
    
    def add_token(self):
        setattr(self, 'token', token_urlsafe(32))