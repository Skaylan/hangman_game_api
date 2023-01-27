from app.controllers.config import *
from app.models.db_config import *
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password_hash = db.Column(db.Text, unique=False, nullable=False)
    global_points = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    last_login = db.Column(db.DateTime(), default=datetime.utcnow)
    biggest_win_streak = db.Column(db.Integer, default=0)
