from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_course_bp(user, clas, content, enroll):
    course_bp = Blueprint('course', __name__,static_folder='static',template_folder='templates')

    @course_bp.route("/course/<id>")
    def course(id):
        if user is None:
            return redirect(url_for('index.index'))

        courseData = clas.get("id='%s'" % (id)).fetchone()
        print(courseData)
        if not courseData :
            res = "Course Data is not Found"
        else :
            res = "Course Data : " + str({k:v for (k,v) in courseData.items()}) + "<br>"

        lecturerData = user.get("id='%s'" % (courseData["lecturer"])).fetchone()
        if not lecturerData :
            res += "Lecturer Data is not Found <br>"
        else :
            res += "Lecturer Data : " + str({k:v for (k,v) in lecturerData.items()}) + "<br>"
        
        courseContent = content.get("courseId='%s'" % (id)).fetchall()
        if not courseContent :
            res += "Course Content Data is not Found <br>"
        else :
            res += "Course Content : " + str(["<br>"+str({k:v for (k,v) in x.items()})+"<br>" for x in courseContent]) + "<br>"

        enrollList = enroll.raw("SELECT users.id, users.status, users.firstName, users.lastName, users.email FROM users INNER JOIN course_enrolls ON course_enrolls.userId = users.id").fetchall()
        if not enrollList :
            res += "enroll Data is not Found <br>"
        else :
            res += "Enrolled Student : " + str(["<br>"+str({k:v for (k,v) in x.items()})+"<br>" for x in enrollList]) + "<br>"

        return(res)

    
    return course_bp