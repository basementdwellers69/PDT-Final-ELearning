from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_student_bp(student):
    student_bp = Blueprint('student', __name__,static_folder='static',template_folder='templates')

    @student_bp.route("/student/<id>")
    def student():
        studentList = student.raw("SELECT users.id, users.status, users.firstName, users.lastName, users.email, marjor.marjor_name FROM users LEFT JOIN major ON majorId = major.id ORDER BY user.id").fetchAll()

        return render_template('student/student.html')
    return student_bp
