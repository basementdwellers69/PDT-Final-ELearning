from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash
import re
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import engine, metadata, db_session, init_db
from models.user import user_model
from models.major import major_model
from controllers.crud import crud_controller
from views.index import construct_index_bp
from views.login import construct_login_bp

#init models
user = user_model(db_session, metadata)
major = major_model(db_session, metadata)

#init database
init_db()
conn = engine.connect()

user_control = crud_controller(conn, user) 
major_control = crud_controller(conn, major) 

index = construct_index_bp(user_control)
login = construct_login_bp(user_control)

app = Flask(__name__,static_url_path='', static_folder='views/static',template_folder='views/templates')
app.register_blueprint(index)
app.register_blueprint(login)

# @app.route('/')
# def index():
#     conn = db_connection()
#     cur = conn.cursor()
#     sql = """
#         SELECT art.id, art.title, art.body, art.user_id
#         FROM articles art
#         ORDER BY art.title
#     """
#     cur.execute(sql)
#     articles = cur.fetchall()
#     cur.close()
#     conn.close()
#     return render_template('index.html', articles=articles)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     """ function to show and process login page """
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         conn = db_connection()
#         cur = conn.cursor()
#         sql = """
#             SELECT id, email, username
#             FROM users
#             WHERE email = '%s' AND password = '%s'
#         """ % (email, password)
#         cur.execute(sql)
#         user = cur.fetchone()
#         print(user)

#         error = ''
#         if user is None:
#             error = 'Wrong credentials. No user found'
#         else:
#             session.clear()
#             session['user_id'] = user[0]
#             session['username'] = user[2]
#             return redirect(url_for('index'))

#         flash(error)
#         cur.close()
#         conn.close()

#     return render_template('login.html')


# @app.route('/logout')
# def logout():
#     """ function to do logout """
#     session.clear()  # clear all sessions
#     return redirect(url_for('index'))

# @app.route('/article/create', methods=['GET', 'POST'])
# def create():
#     # check if user is logged in
#     if not session:
#         return redirect(url_for('login'))

#     if request.method == 'POST':
#         data = request.get_json() or {}
#         # check existence of title and body
#         if data.get('title') and data.get('body'):
#             title = data.get('title', '')
#             body = data.get('body', '')
#             user_id = session.get('user_id')

#             # strip() is to remove excessive whitespaces before saving
#             title = title.strip()
#             body = body.strip()

#             conn = db_connection()
#             cur = conn.cursor()
#             # insert with the user_id
#             sql = """
#                 INSERT INTO articles (title, body, user_id) VALUES ('%s', '%s', %d)
#             """ % (title, body, user_id)
#             cur.execute(sql)
#             conn.commit()  # commit to make sure changes are saved
#             cur.close()
#             conn.close()
#             # an example with redirect
#             print("success")
#             return jsonify({'status': 200, 'message': 'Success', 'redirect': '/'})

#         # else will be error
#         print("error")
#         return jsonify({'status': 500, 'message': 'No Data submitted'})

#     return render_template('create.html')