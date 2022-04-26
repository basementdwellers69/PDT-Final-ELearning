from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_student_bp(controller):
    student_bp = Blueprint('student', __name__,static_folder='static',template_folder='templates')

    @student_bp.route("/student")
    def student():
        studentList = controller.raw("SELECT users.id, users.status, users.firstName, users.lastName, users.email, majors.majorName FROM users LEFT JOIN majors ON majorId = majors.id ORDER BY users.id").fetchall()

        return render_template('student/student.html', stud=studentList)
    return student_bp
