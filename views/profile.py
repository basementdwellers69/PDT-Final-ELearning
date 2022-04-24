from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_profile_bp(controller):
    profile_bp = Blueprint('profile', __name__,static_folder='static',template_folder='templates')

    @profile_bp.route("/profile")
    def profile():
        return render_template('profile/profile.html')

    
    return profile_bp