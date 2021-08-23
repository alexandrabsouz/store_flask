import os

from flask import flash, redirect, render_template, request, session, url_for
from store import app, bcrypt, db

from .form import RegistrationForm, LoginForm
from .models import User


@app.get('/admin')
def admin():
    if 'email' not in session:
        flash('login first', 'danger')
        return redirect(url_for('login'))
    
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



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash('Welcome!', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('[ERRO]: Invalid email or password', 'danger')
            
    return render_template('admin/login.html', form=form, title='Login')
    