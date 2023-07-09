from .database import db
from sqlalchemy import Column, Integer, String


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String(100))
    username = Column(String(50))

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username
