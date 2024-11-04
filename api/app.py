from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Pune',
        'salary': 'Rs.100000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi',
        'salary': 'Rs.150000'
    },
    {
        'id': 4,
        'title': 'AI Researcher',
        'location': 'Remote',
        'salary': 'Rs.200000'
    },
    {
        'id': 4,
        'title': 'Frontend Engineer',
        'location': 'San Fransico',
        'salary': '$120000'
    }
]


@app.route("/")
def hello_world():
    # return "<p> Hello angkul</p>"
    return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)