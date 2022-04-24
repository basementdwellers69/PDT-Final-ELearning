from flask import Blueprint, render_template, request
import sys

def construct_login_bp(controller):
    login_bp = Blueprint('login', __name__,static_folder='static',template_folder='templates')

    @login_bp.route("/login", methods=['GET','POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            query = "email='%a' and password='%b'" % (email, password)
            user = controller.get(query)
            if user.count() != 0:
                error = 'Wrong credentials. No user found'
            else:
                session.clear()
                session['user_id'] = user[0]
                session['username'] = user[2]
                return redirect(url_for('index.index'))

            flash(error)
            cur.close()
            conn.close()

        return render_template('login/login.html')
        
    
    return login_bp