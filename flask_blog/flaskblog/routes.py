from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


# adding dummy data
posts = [
    {
        'author': 'Angkul',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date': '09-Nov-2024'
    },
    {
        'author': 'Keshav',
        'title': 'Blog Post 2',
        'content': '2nd post content',
        'date': '13-Nov-2024'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))

    return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data=='1234':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login faild', 'danger')
    return render_template('login.html', title = 'Login', form=form)