	from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_inputcourse_bp(controller):
    inputcourse_bp = Blueprint('inputcourse', __name__,static_folder='static',template_folder='templates')

    @inputcourse_bp.route("/course/input")
   
#
#
        return render_template('inputcourse/inputcourse.html')
    return inputcourse_bp
