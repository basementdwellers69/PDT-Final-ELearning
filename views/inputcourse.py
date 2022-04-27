
from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_inputcourse_bp(controller):
    inputcourse_bp = Blueprint('inputcourse', __name__,static_folder='static',template_folder='templates')

    @inputcourse_bp.route("/inputcourse", methods=['GET', 'POST'])
    def inputcourse():
        if request.method == 'POST' and 'courseName' in request.form and 'courseId' in request.form and 'courseDescription' in request.form:
            courseName = request.form['courseName']
            courseId = request.form['courseId']
            courseDescription = request.form['courseDescription']
            lecturer = session['user_id']
            major = session['user_major']

            incourse = controller.raw("INSERT INTO courses (majorId, courseName, courseDescription, lecturer VALUES (%s, '%s', '%s', %s)" % (major, courseName, courseDescription, lecturer)) 
            #incourse.commit()
            #print(incourse, file=sys.stdout)
        else:
            print('error')

        return render_template('inputcourse/inputcourse.html')

    return inputcourse_bp
