from . import auth
import os 
from flask import render_template, session, redirect, url_for, flash, request, jsonify, session
from app.models import User
import datetime
from flasgger import swag_from
import jwt
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required , unset_jwt_cookies
 
secret_jwt = os.environ.get("SECRET_JWT")


@auth.route('/decode')
@swag_from("../../documentation/decode.yaml")
def index():
    try:
        bearer = request.headers.get("Authorization").split()[1]
        return jwt.decode(bearer, secret_jwt , algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {

            'error': f'{jwt.ExpiredSignatureError}',

            'message': 'Signature expired. Please log in again.'

        }, 500
    except jwt.InvalidTokenError:
         return {

            'error': f'{jwt.InvalidTokenError}',

            'message': 'Invalid token. Please log in again.'

        }, 500

@auth.route("/rok")
@jwt_required()
def rok():
    try:
        return {
            'succesfully': 'your json-jwt its allowed'
        }
    except Exception as e:
        return {
            "message": e
        }



@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
@swag_from("../../documentation/refresh.yaml")
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


@auth.route("/logout", methods=["POST"])
@swag_from("../../documentation/logout.yaml")
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@auth.route('/login', methods=["POST"])
@swag_from("../../documentation/login.yaml")
def login():

    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
    
        user = User.query.filter_by(email=email).one_or_none()
    
        if not user:
            return {
                
                'message': f'User {email} doesn\'t exist'
                
            }, 401
        
        if User.verify_hash(password, user.password):
            
            access_token = create_access_token(identity=email)
            
            refresh_token = create_refresh_token(identity=email)

            return {

                'message': f'User {email} is login now',

                'access_token': access_token,

                'refresh_token': refresh_token

            }, 200

        else:
            return {
            
                'message': "Wrong credentials"
            
            }, 401

    except Exception as e:
        return {

            'error': f'{e}',

            'message': "Something went wrong"

        }, 500


# posible implementation in the future
@auth.route('/create_account', methods=["POST"])
@swag_from("../../documentation/create_account.yaml")
def create_account():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        
        user = User.query.filter_by(email=email).one_or_none()
        
        if user != None:
            return {
                
                'message': f'user {email} already exists'
                
            }, 401
        
        new_user = User(email=email, password= User.generate_hash(password))
        
        try:
            new_user.save_to_db()
            
            access_token = create_access_token(identity=email)
            
            refresh_token = create_refresh_token(identity=email)

            return {

                'message': f'User {email} was created',

                'access_token': access_token,

                'refresh_token': refresh_token

            }, 201

        except Exception as e:
            return {

                'error': f'{e}',

                'message': "Something went wrong"

            }, 500

    except Exception as e:
        return {
            
            'error': f'{e}',

            'message': "Something went wrong"

        }, 500
