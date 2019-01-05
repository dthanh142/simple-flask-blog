from app import app
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app.loginForm import LoginForm
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


