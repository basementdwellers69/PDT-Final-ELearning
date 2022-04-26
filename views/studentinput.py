from crypt import methods
from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_studentinput_bp(controller):
    studentinput_bp = Blueprint('studentinput', __name__,static_folder='static',template_folder='templates')

    @studentinput_bp.route('/studentinput', methods=['GET', 'POST'])
    def studentinput():
        #if request.method == 'POST':
        #    firstname = request.form['firstname']
        #    lastname = request.form['lastname']
        #    address = request.form['address']
        #    country = request.form['country']
        #    city = request.form['city']
        #    postalcode = request.form['postalcode']

        #    username = request.form['username']
        #    email = request.form['email']
        #    password = request.form['password']
        #    status = request.form['status']
        #    major = request.form['major']

            #check if account exists
        #    query = "username = '%s'" % (username)
        #    stmp = controller.get(query)
        #    user = stmp.fetchone()
        #    print(user)

        #    if user:
        #        flash('Account already exists!')
        #    else:
            #account doesn't exists insert to database
        #        input = controller.raw("INSERT INTO users (firstName, lastName, address, country, city, postalCode, username, email, password, status, majorId) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %s)")
                
        #        flash('You have successfully registered!')
                
        return render_template('studentinput/studentinput.html')

    return studentinput_bp
                