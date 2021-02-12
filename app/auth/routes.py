from . import auth
from flask import render_template, session, redirect, url_for, flash, request
import jwt

@auth.route('/auth')
def index():
    bearer = request.headers.get("Authorization").split()[1]
    try:
        return jwt.decode(bearer, "0YsAxFFsjbR6O1pORbNDmpHbq4zwWoJtbhIyCYYKGylL3o6knuUF0FXTVDpG80Dz", algorithms=["HS256"])
    except: 
        return redirect(url_for('auth.index'))