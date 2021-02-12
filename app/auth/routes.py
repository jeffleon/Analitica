from . import auth
from flask import render_template, session, redirect, url_for, flash


@auth.route('/auth')
def index():
    return render_template('auth.html')