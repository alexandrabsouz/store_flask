from flask import render_template, session, request, url_for
from flask_wtf import flash, redirect
from .form import RegistrationForm
from store import app, db 


@app.get('/')
def index():
    return {'store': 'My store index route'}


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
                    #form.password.data)
        #db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)