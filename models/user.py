from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

def user_model(db_session, metadata):

    class User(object):
        query = db_session.query_property()

        def __init__(self, name=None, email=None):
            self.name = name
            self.email = email

        def __repr__(self):
            return f'<User {self.name!r}>'

    users = Table('users', metadata,
        Column('id', Integer, primary_key=True),
        Column('status', Integer, unique=False),
        Column('firstName', String(30), unique=False, nullable=False),
        Column('lastName', String(30), unique=False),
        Column('email', String(120), unique=False, nullable=False),
        Column('password', String(30), unique=False, nullable=False),
        Column('majorId', Integer, unique=False)
    )
    mapper(User, users)
    return users