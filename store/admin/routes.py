import os

from flask import flash, redirect, render_template, request, session, url_for
from store import app, bcrypt, db

from .form import RegistrationForm
from .models import User


@app.get('/')
def index():
    return render_template('admin/index.html', title='Admin Page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, email=form.email.data,
                    password=hash_password)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Thanks for registering', 'success')
        return redirect(url_for('index'))
    
    return render_template('admin/register.html', form=form, title='Register')




    