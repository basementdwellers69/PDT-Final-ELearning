from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_profile_bp(controller):
    profile_bp = Blueprint('profile', __name__,static_folder='static',template_folder='templates')

    @profile_bp.route("/profile")
    def profile():
        query = "SELECT users.id, users.status, users.firstName, users.lastName, users.email, majors.majorName FROM `users` INNER JOIN majors ON majors.id=users.majorId;"
        stmp = controller.raw(query)
        stmp.fetchall()
        return render_template('profile/profile.html')

    
    return profile_bp