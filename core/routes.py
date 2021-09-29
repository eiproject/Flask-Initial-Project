from . import app, jwt
from .models import User

from flask import Flask, request, render_template, redirect, jsonify

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


@app.route("/jwt-test", methods=["GET"])
@jwt_required()
def protected():
    if request.method == 'GET':
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        print('current_user: ', current_user)
        if current_user:
            return jsonify(msg="Logged in, {}".format(current_user)), 200

    else:
        return jsonify({"msg": "Bad API Method"}), 401


# Custom JWT Response
@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'code': 401,
        'status': 'ERROR',
        'data': [
            {'error': 'The token has expired'}
        ]
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(invalid_token):
    return jsonify({
        'code': 422,
        'status': 'ERROR',
        'data': [
            {'error': 'Signature verification failed'}
        ]
    }), 422


@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({
        'code': 413,
        'status': 'ERROR',
        'data': [
            {'error': 'File too large'}
        ]
    }), 413
