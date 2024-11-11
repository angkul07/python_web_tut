from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)