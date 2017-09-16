#!flask/bin/python

import string
import sys

from flask import Flask, jsonify, redirect, request, abort
import registry_authz.authorization.endpoint
app = Flask(__name__)


@app.route('/')
def index():
    return "Index"

@app.route('/authorized', methods=['POST'])
def is_authorized():
    "Check if request is authorized"
    print("stub")
    registry_authz.authorization.endpoint.is_authorized(request)


@app.route('/add-role', methods=['POST'])
def add_role():
    "Adding some roles"
    print("stub")


@app.route('/delete-role', methods=['POST'])
def delete_role():
    "deleting some roles"
    print("stub")

@app.route('/add-role-binding', methods=['POST'])
def add_role_binding():
    "Adding some role bindings"
    print("stub")


@app.route('/delete-role-binding', methods=['POST'])
def delete_role_binding():
    "Deleting some role bindings"
    print("stub")


def run():
    """Entry point for console_scripts
    """
    app.run(host='0.0.0.0')

