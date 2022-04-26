from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_viewmaterial_bp(controller):
    viewmaterial_bp = Blueprint('viewmaterial', __name__,static_folder='static',template_folder='templates')

    @viewmaterial_bp.route("/course/<int:id>/viewmaterial")
    def viewmaterial():
        viewmaterial = controller.raw("SELECT * FROM 'course_content'").fetchall()

        return render_template('viewmaterial/viewmaterial.html', viewMat=viewmaterial)
    return viewmaterial_bp
