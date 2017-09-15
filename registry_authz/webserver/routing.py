#!flask/bin/python

import string
import sys

from flask import Flask, jsonify, redirect, request, abort

app = Flask(__name__)


@app.route('/')
def index():
    return "Index"


def run():
    """Entry point for console_scripts
    """
    app.run(host='0.0.0.0')

