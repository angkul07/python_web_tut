from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'acc44fa13af8da5d55cc3e3c994ef536'

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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)