from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_classes_bp(user, clas, content, enroll):
    classes_bp = Blueprint('classes', __name__,static_folder='static',template_folder='templates')

    @classes_bp.route("/class/<id>")
    def classes(id):
        if user is None:
            return redirect(url_for('index.index'))

        classData = clas.get("id='%s'" % (id)).fetchone()
        res = "Class Data : " + str({k:v for (k,v) in classData.items()}) + "<br>"

        lecturerData = user.get("id='%s'" % (classData["lecturer"])).fetchone()
        res += "Lecturer Data : " + str({k:v for (k,v) in lecturerData.items()}) + "<br>"
        
        classContent = content.get("classId='%s'" % (id)).fetchall()
        res += "Class Content : " + str(["<br>"+str({k:v for (k,v) in x.items()})+"<br>" for x in classContent]) + "<br>"

        enrollList = enroll.raw("SELECT users.id, users.status, users.firstName, users.lastName, users.email FROM users INNER JOIN class_enrolls ON class_enrolls.userId = users.id").fetchall()
        res += "Enrolled Student : " + str(["<br>"+str({k:v for (k,v) in x.items()})+"<br>" for x in enrollList]) + "<br>"

        return(res)

    
    return classes_bp