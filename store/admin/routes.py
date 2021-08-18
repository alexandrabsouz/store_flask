from flask import render_template, session, request, url_for, flash, redirect
from .form import RegistrationForm
from store import app, db, bcrypt
from .models import User
import os


@app.get('/')
def index():
    return {'store': 'My store index route'}


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data,
                    password=hash_password)
        
        db.session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('admin/register.html', form=form, title='Register')