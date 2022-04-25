from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_course_bp(user, clas, content, enroll):
    course_bp = Blueprint('course', __name__,static_folder='static',template_folder='templates')

    @course_bp.route("/course/<id>")
    def course(id):
        if user is None:
            return redirect(url_for('index.index'))

        courseData = clas.get("id='%s'" % (id)).fetchone()
        res = "Course Data : " + str({k:v for (k,v) in courseData.items()}) + "<br>"

        lecturerData = user.get("id='%s'" % (courseData["lecturer"])).fetchone()
        res += "Lecturer Data : " + str({k:v for (k,v) in lecturerData.items()}) + "<br>"
        
        courseContent = content.get("courseId='%s'" % (id)).fetchall()
        res += "Course Content : " + str(["<br>"+str({k:v for (k,v) in x.items()})+"<br>" for x in courseContent]) + "<br>"

        enrollList = enroll.raw("SELECT users.id, users.status, users.firstName, users.lastName, users.email FROM users INNER JOIN course_enrolls ON course_enrolls.userId = users.id").fetchall()
        res += "Enrolled Student : " + str(["<br>"+str({k:v for (k,v) in x.items()})+"<br>" for x in enrollList]) + "<br>"

        return(res)

    
    return course_bp