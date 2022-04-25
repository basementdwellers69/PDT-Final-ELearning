from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.orm import mapper

def class_model(db_session, metadata):

    class Class(object):
        query = db_session.query_property()

        def __init__(self, className=None):
            self.className = className

        def __repr__(self):
            return f'<class {self.className!r}>'

    classes = Table('classes', metadata,
        Column('id', Integer, primary_key=True),
        Column('majorId', Integer, unique=False),
        Column('className', String(50), unique=False, nullable=False),
        Column('classDescription', String(200), unique=False, nullable=False),
        Column('lecturer', Integer, unique=False, nullable=False)
    )
    mapper(Class, classes)
    return classes

def class_content_model(db_session, metadata):

    class ClassContent(object):
        query = db_session.query_property()

        def __init__(self, classId=None):
            self.classId = classId

        def __repr__(self):
            return f'<ClassContent {self.classId!r}>'

    class_contents = Table('class_contents', metadata,
        Column('id', Integer, primary_key=True),
        Column('classId', Integer, unique=False, nullable=False),
        Column('type', Integer, unique=False, nullable=False),
        Column('contentTitle', String(50), unique=False, nullable=False),
        Column('contentBody', String(200), unique=False, nullable=False),
        Column('create_time', DateTime, unique=False, nullable=False),
        Column('status', Integer, unique=False, default=0)
    )
    mapper(ClassContent, class_contents)
    return class_contents

def class_enroll_model(db_session, metadata):

    class ClassEnroll(object):
        query = db_session.query_property()

        def __init__(self, classId=None):
            self.classId = classId

        def __repr__(self):
            return f'<ClassEnroll {self.classId!r}>'

    class_enrolls = Table('class_enrolls', metadata,
        Column('id', Integer, primary_key=True),
        Column('classId', Integer, unique=False, nullable=False),
        Column('userId', Integer, unique=False, nullable=False),
        Column('status', Integer, unique=False, default=0),
    )
    mapper(ClassEnroll, class_enrolls)
    return class_enrolls