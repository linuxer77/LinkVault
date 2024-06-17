from flask import render_template, flash, redirect, url_for, request
from urllib.parse import urlsplit
from main import app, db
from main.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from main import db
from main.models import User

@app.route('/vault')
def vault():
    return render_template('vault.html', title='vault')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Link Vault - Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Link Vault - Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
 
'''Key Points to Remember

    sa (SQLAlchemy Core):
        Used for raw SQL-like tasks.
        Define tables, columns, and database schemas.
        Use when you need fine-grained control over your SQL.

    so (SQLAlchemy ORM):
        Used for working with Python classes and objects.
        Define classes that map to tables, and manage relationships.
        Use when you prefer working with objects rather than raw SQL.'''