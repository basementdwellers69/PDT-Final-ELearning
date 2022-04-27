from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_profile_bp(controller):
    profile_bp = Blueprint('profile', __name__,static_folder='static',template_folder='templates')

    @profile_bp.route("/profile")
    def profile():
        user_id = session.get('user_id')
        # query = "id = %s" % (user_id)
        # stmp = controller.get(query)
        # profile = stmp.fetchone()

        profile = controller.raw("SELECT users.id, users.status, users.firstName, users.lastName, users.username, users.email, users.address, users.city, users.country, users.postalCode, users.aboutMe, majors.majorName FROM users LEFT JOIN majors ON majorId = majors.id WHERE users.id = %s ORDER BY users.id" % (user_id)).fetchone()

        print(profile, file=sys.stdout)
        
        session['firstname'] = profile['firstName']
        session['lastname'] = profile['lastName']
        session['stdusername'] = profile['username']
        session['email'] = profile['email']
        session['address'] = profile['address']
        session['city'] = profile['city']
        session['country'] = profile['country']
        session['postal'] = profile['postalCode']
        session['about'] = profile['aboutMe']
        session['major'] = profile['majorName']

        return render_template('profile/profile.html')
    return profile_bp