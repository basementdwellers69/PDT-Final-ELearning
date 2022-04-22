from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

def major_model(db_session, metadata):

    class Major(object):
        query = db_session.query_property()

        def __init__(self, majorName=None):
            self.majorName = majorName

        def __repr__(self):
            return f'<Major {self.majorName!r}>'

    majors = Table('majors', metadata,
        Column('id', Integer, primary_key=True),
        Column('majorName', String(200), unique=False, nullable=False)
    )
    mapper(Major, majors)
    return majors