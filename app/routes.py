from app import app, db
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app.loginForm import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'thanhdp'}
    posts = [
        {
            'author': {'username': 'thanhdp'},
            'body': 'What a cold day'
        },
        {
            'author': {'username': 'minhnguyenhu'},
            'body': 'Gimmie a hug'
        }
    ]
    return render_template('index.html', title='', posts=posts)


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        # url_parse().netloc checks if the next_page query argument redirect to another site with fully domain name set
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        # flash('Login requested for user {}, password={} remember_me={}'.format(
        #     form.username.data, form.password.data, form.remember_me.data
        # ))
        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)


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
        flash('Successfully registered, please login again')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        { 'author': user, 'body': 'Hi, im {}'.format(user.username) },
        { 'author': user, 'body': 'What a noice day' }
    ]
    return render_template('user.html', user=user, posts=posts)