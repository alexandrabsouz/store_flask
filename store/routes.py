from flask import render_template, session, request, url_for

from store import app, db 


@app.get('/')
def index():
    return {'store': 'My store index route'}


