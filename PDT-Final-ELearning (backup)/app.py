
import string
from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash
import re
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash

from db import db_connection

app = Flask(__name__)
app.secret_key = 'THISISMYSECRETKEY'


@app.route('/')
def index():
    conn = db_connection()
    cur = conn.cursor()
    sql2 = """
        SELECT courses.id, courses.name, courses.lecturerId
        FROM courses
    """
    
    cur.execute(sql2)
    print(sql2)
    courses = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', courses=courses)

def index2():
    conn = db_connection()
    cur = conn.cursor()
    sql = """
        SELECT art.id, art.title, art.body, art.user_id
        FROM articles art
        ORDER BY art.title
    """
    cur.execute(sql)

    articles = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', articles=articles)



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
        print(user)

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

@app.route('/article/create', methods=['GET', 'POST'])
def create():
    # check if user is logged in
    if not session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        data = request.get_json() or {}
        # check existence of title and body
        if data.get('title') and data.get('body'):
            title = data.get('title', '')
            body = data.get('body', '')
            user_id = session.get('user_id')

            # strip() is to remove excessive whitespaces before saving
            title = title.strip()
            body = body.strip()

            conn = db_connection()
            cur = conn.cursor()
            # insert with the user_id
            sql = """
                INSERT INTO articles (title, body, user_id) VALUES ('%s', '%s', %d)
            """ % (title, body, user_id)
            cur.execute(sql)
            conn.commit()  # commit to make sure changes are saved
            cur.close()
            conn.close()
            # an example with redirect
            print("success")
            return jsonify({'status': 200, 'message': 'Success', 'redirect': '/'})

        # else will be error
        print("error")
        return jsonify({'status': 500, 'message': 'No Data submitted'})

    return render_template('create.html')

@app.route('/profile', methods=['GET'])
def profile():
    conn = db_connection()
    cur = conn.cursor()
    user_id = session.get('user_id')
    sql = """
        SELECT users.username, users.email, users.firstname, users.lastname, users.address, users.city, users.country, users.postalcode, users.aboutme, major.major_name FROM users
        LEFT JOIN major
        ON users.majorId = major.id
        WHERE users.id = %s
        ORDER BY users.username;
    """ % (user_id)
    
    print(sql)
    
    cur.execute(sql)
    profile = cur.fetchone()
    
    cur.close()
    conn.close()

    return render_template ('profile.html', profile=profile)

@app.route('/students')
def students():
    conn = db_connection()
    cur = conn.cursor()
    
    sql = """
        SELECT usr.id, usr.firstname, usr.lastname, usr.email, major.major_name, courses.name FROM users usr
        LEFT JOIN major
        ON usr.majorId = major.id
        LEFT JOIN courses 
        ON usr.courseId = courses.id
        ORDER BY usr.id;
    """
    
    cur.execute(sql)
    student = cur.fetchall()
    print(student)
    cur.close()
    conn.close()

    return render_template('student.html', student=student)

@app.route('/student/view/<int:student_id>', methods=['GET'])
def read(student_id):
    
    conn = db_connection()
    cur = conn.cursor()
    sql = """
        SELECT users.username, users.email, users.firstname, users.lastname, users.address, users.city, users.country, users.postalcode, users.aboutme, major.major_name FROM users
        LEFT JOIN major
        ON users.majorId = major.id
        WHERE users.id = %s
        ORDER BY users.username;
    """ % (student_id)
    cur.execute(sql)
    student = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('studentview.html', profile=student)

@app.route('/student/edit/<int:student_id>', methods=['GET', 'POST'])
def edit(student_id):
    # check if user is logged in
    if not session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        conn = db_connection()
        cur = conn.cursor()
        username = request.form['username']
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address = request.form['address']
        city = request.form['city']
        country = request.form['country']
        postalcode = request.form['postalcode']
        aboutme = request.form['aboutme']

        username = username.strip()
        email = email.strip()
        firstname = firstname.strip()
        lastname = lastname.strip()
        address = address.strip()
        city = city.strip()
        country = country.strip()
        postalcode = postalcode.strip()
        aboutme = aboutme.strip()

        sql_params = (username, email, firstname, lastname, address, city, country, postalcode, aboutme, student_id)

        sql = "UPDATE users SET username = '%s', email = '%s', firstname = '%s', lastname = '%s', address = '%s', city = '%s', country= '%s', postalcode = '%s', aboutme = '%s' WHERE id = %s" % sql_params
        
        print(student_id)
        cur.execute(sql)
        conn.commit()

        cur.close()
        conn.close()
        # use redirect to go to certain url. url_for function accepts the
        # function name of the URL which is function index() in this case
        return redirect(url_for('students'))

    # find the record first
    conn = db_connection()
    cur = conn.cursor()
    sql = 'SELECT username, email, firstname, lastname, address, city, country, postalcode, aboutme FROM users WHERE id = %s' % student_id
    cur.execute(sql)
    student = cur.fetchone()
    cur.close()
    conn.close()

    return render_template('studentedit.html', profile=student)

@app.route('/student/delete/<int:student_id>', methods=['GET', 'POST'])
def delete(student_id):
    # check if user is logged in
    if not session:
        return redirect(url_for('login'))

    conn = db_connection()
    cur = conn.cursor()
    sql = 'DELETE FROM users WHERE id = %s' % student_id
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
    return render_template('students')

@app.route('/newstudent', methods=['GET', 'POST'])
def newstudent():
    if not session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        conn = db_connection()
        cur = conn.cursor()
        
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address = request.form['address']
        country = request.form['country']
        city = request.form['city']
        postalcode = request.form['postalCode']
        
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        status = request.form['status']
        major = request.form['major']

        username = username.strip()
        email = email.strip()
        firstname = firstname.strip()
        lastname = lastname.strip()
        address = address.strip()
        city = city.strip()
        country = country.strip()
        postalcode = postalcode.strip()
        status = status.strip()
        major = major.strip()
        

        sql_params = (firstname, lastname, address, country, city, postalcode, username, email, password, status, major)

        sql = "INSERT INTO users (firstname, lastname, address, country, city, postalcode, username, email, password, status, majorId) VALUES ('%s', '%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', %s, %s)" % sql_params
        
        print(sql)

        cur.execute(sql)
        conn.commit()

        cur.close()
        conn.close()
        return redirect(url_for('students'))

    return render_template('studentinput.html')

@app.route('/assignment')
def assignment():
    return render_template('assignment.html')

@app.route('/course/<int:courseId>')
def course(courseId):
    conn = db_connection()
    cur = conn.cursor()
    sql = """
        SELECT con.id, con.title, con.link, con.courseId, courses.name, courses.room, courses.classlink, users.id, users.firstname, users.lastname FROM course_content con
        LEFT JOIN courses 
        ON con.courseId = courses.id 
        LEFT JOIN users ON lecturerId = users.id
        WHERE courses.id = %s
    """ % (courseId)
    
    cur.execute(sql)
    print(sql)
    content = cur.fetchone()
    cur.close()
    conn.close()
    return render_template ('course.html', content=content)

@app.route('/course/addmaterial', methods=['GET', 'POST'])
def material():
    if not session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        conn = db_connection()
        cur = conn.cursor()

        coursetitle = request.form['coursetitle']
        courselink = request.form['courselink']

        coursetitle = coursetitle.strip()
        courselink = courselink.strip()

        sql= """
            INSERT INTO course_content (title, link) 
            VALUES ('%s', '%s') """ % (coursetitle, courselink)

        cur.execute(sql)
        conn.commit()

        cur.close()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('inputmateri.html')

@app.route('/addclass', methods=['GET', 'POST'])
def addclass():
    if not session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_id = session['user_id']
        conn = db_connection()
        cur = conn.cursor()

        classname = request.form['classname']
        classroom = request.form['classroom']
        classlink = request.form['classlink']

        sql = """
            INSERT INTO courses (name, lecturerId, room, classlink) 
            VALUES ('%s', %s, '%s', '%s')""" % (classname, user_id, classroom, classlink)

        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('addclass.html')

