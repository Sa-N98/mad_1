from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name =db.Column(db.String)
    email =db.Column(db.String)
    password =db.Column(db.String)
    user_type =db.Column(db.String)

class movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name =db.Column(db.String)
    genre =db.Column(db.String)
    poster =db.Column(db.String)
    
    