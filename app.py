from flask import Flask, request, render_template, session, flash, redirect, url_for, jsonify
import re
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash


from db import db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ function to show and process login page """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = db_connection()
        cur = conn.cursor()
        sql = """
            SELECT id, email, username
            FROM users
            WHERE email = '%s' AND password = '%s'
        """ % (email, password)
        cur.execute(sql)
        user = cur.fetchone()

        error = ''
        if user is None:
            error = 'Wrong credentials. No user found'
        else:
            session.clear()
            session['user_id'] = user[0]
            session['username'] = user[2]
            return redirect(url_for('index'))

        flash(error)
        cur.close()
        conn.close()

    return render_template('login.html')

@app.route('/logout')
def logout():
    """ function to do logout """
    session.clear()  # clear all sessions
    return redirect(url_for('index'))


