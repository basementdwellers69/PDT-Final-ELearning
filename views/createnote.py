from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys


def construct_createnote_bp(controller):
    createnote_bp = Blueprint('createnote', __name__,static_folder='static',template_folder='templates')

    @createnote_bp.route('/createnote', methods=['GET', 'POST'])
    def createnote():
        # check if user is logged in
        #if not session:
            #return redirect(url_for('login'))

        #if request.method == 'POST':
        #    title = request.form['title']
        #    body = request.form['body']

        #    createnote = controller.raw("INSERT INTO articles (title, body) VALUES ('%s', '%s')" % (title, body))
            

        return render_template('createnote/createnote.html', createnote=createnote)