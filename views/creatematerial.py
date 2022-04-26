from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_creatematerial_bp(controller):
    creatematerial_bp = Blueprint('creatematerial', __name__,static_folder='static',template_folder='templates')

    @creatematerial_bp.route("/course/<id>/creatematerial", methods = ['GET','POST'])
    def creatematerial():

            # if request.method == 'POST':
            #     Id = request.form['id']
            #     courseId = request.form['courseId']
            #     type = request.form['type']
            #     contentTitle = request.form['contentTitle']
            #     contentBody = request.form['contentBody']
            #     create_time = request.form['create_time']
            #     status = request.form['status']

            #     query = "contentTitle = '%s'" % (contentTitle)
            #     stmp = controller.get(query)
            #     materi = stmp.fetchone()
            #     print(materi)

            #     if materi:
            #         flash('Material already exists!')

            #     else:
            #         input = controller.raw("INSERT INTO course_contents (id, courseId, type, contentTitle, contentBody, create_time, status) VALUES (%s, %s, %s, '%s', '%s', '%s', %s)")
                
            #         flash('You have successfully registered!')

        return render_template('creatematerial/creatematerial.html', cMat=creatematerial)
    
    return creatematerial_bp
