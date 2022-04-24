from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_login_bp(controller):
    login_bp = Blueprint('login', __name__,static_folder='static',template_folder='templates')

    @login_bp.route("/login", methods=['GET','POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            query = "email='%s' and password='%s'" % (email, password)
            stmp = controller.get(query)
            user = stmp.fetchone()
            print(user, file=sys.stdout)
            if user is None:
                error = 'Wrong credentials. No user found'
            else:
                session.clear()
                session['user_id'] = user["id"]
                session['user_status'] = user["status"]
                session['user_major'] = user["majorId"]
                return redirect(url_for('index.index'))

            flash(error)

        return render_template('login/login.html')

    @login_bp.route('/logout')
    def logout():
        session.clear()  # clear all sessions
        return redirect(url_for('index.index'))
        
    
    return login_bp