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

