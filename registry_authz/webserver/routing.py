#!flask/bin/python

import string
import sys

from flask import Flask, jsonify, redirect, request, abort

app = Flask(__name__)


@app.route('/')
def index():
    return "Index"


def main(args):
    app.run(host='0.0.0.0')


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == '__main__':
    run()
