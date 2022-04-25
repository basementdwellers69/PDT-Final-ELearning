from sqlalchemy import Table, Column, Integer, String, Text
from sqlalchemy.orm import mapper

def user_model(db_session, metadata):

    class User(object):
        query = db_session.query_property()

        def __init__(self, status=0, firstName=" ", lastName=" ", email=" ", password=" ", majorId=0, address=None, city=None, country=None, postalCode=None, aboutMe=None):
            self.status = status
            self.firstName = firstName
            self.lastName = lastName
            self.address = address
            self.city = city
            self.address = address
            self.city = city
            self.country = country
            self.postalCode = postalCode
            self.aboutMe = aboutMe
            self.email = email
            self.password = password
            self.majorId = majorId

        def __repr__(self):
            return f'<User {self.status!r}>'

    users = Table('users', metadata,
        Column('id', Integer, primary_key=True),
        Column('status', Integer, unique=False),
        Column('firstName', String(30), unique=False, nullable=False),
        Column('lastName', String(30), unique=False, nullable=False),
        Column('address', String(300), unique=False),
        Column('city', String(250), unique=False),
        Column('country', String(250), unique=False),
        Column('postalCode', Integer, unique=False),
        Column('aboutMe', Text, unique=False),
        Column('email', String(120), unique=False, nullable=False),
        Column('password', String(30), unique=False, nullable=False),
        Column('majorId', Integer, unique=False, nullable=False)
    )
    mapper(User, users)
    return users