from sqlalchemy import Table, Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import mapper

def course_model(db_session, metadata):

    class Course(object):
        query = db_session.query_property()

        def __init__(self, majorId=0, courseName="Course", courseDescription="Course Description", lecturer=1):
            self.majorId = majorId
            self.courseName = courseName
            self.courseDescription = courseDescription
            self.lecturer = lecturer

        def __repr__(self):
            return f'<course {self.majorId!r}>'

    courses = Table('courses', metadata,
        Column('id', Integer, primary_key=True),
        Column('majorId', Integer, unique=False, nullable=False),
        Column('courseName', String(50), unique=False, nullable=False),
        Column('courseDescription', String(200), unique=False, nullable=False),
        Column('lecturer', Integer, unique=False, nullable=False)
    )
    mapper(Course, courses)
    return courses

def course_content_model(db_session, metadata):

    class CourseContent(object):
        query = db_session.query_property()

        def __init__(self, courseId=0, type=0, contentTitle="Title", contentBody="Body", status=0, create_time=datetime.now()):
            self.courseId = courseId
            self.type = 0,
            self.contentTitle = contentTitle
            self.contentBody = contentBody
            self.status = status
            self.create_time = create_time

        def __repr__(self):
            return f'<CourseContent {self.courseId!r}>'

    course_contents = Table('course_contents', metadata,
        Column('id', Integer, primary_key=True),
        Column('courseId', Integer, unique=False, nullable=False),
        Column('type', Integer, unique=False, nullable=False),
        Column('contentTitle', String(50), unique=False, nullable=False),
        Column('contentBody', String(200), unique=False, nullable=False),
        Column('create_time', DateTime, unique=False, nullable=False),
        Column('status', Integer, unique=False, default=0)
    )
    mapper(CourseContent, course_contents)
    return course_contents

def course_enroll_model(db_session, metadata):

    class CourseEnroll(object):
        query = db_session.query_property()

        def __init__(self, courseId=0, userId=1, status=1):
            self.courseId = courseId
            self.userId = userId
            self.status = status

        def __repr__(self):
            return f'<CourseEnroll {self.courseId!r}>'

    course_enrolls = Table('course_enrolls', metadata,
        Column('id', Integer, primary_key=True),
        Column('courseId', Integer, unique=False, nullable=False),
        Column('userId', Integer, unique=False, nullable=False),
        Column('status', Integer, unique=False, default=0),
    )
    mapper(CourseEnroll, course_enrolls)
    return course_enrolls