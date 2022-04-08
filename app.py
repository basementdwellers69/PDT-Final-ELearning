from flask import Flask, request, render_template, session, flash, redirect, url_for, jsonify
import re
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash


from db import db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')