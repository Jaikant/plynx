#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def urls_for():
    pass
    url_for('static', filename='style.css')
    url_for('static', filename='favicon.png')

