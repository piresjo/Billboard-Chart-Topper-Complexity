from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/hot100')
def hot100():
    return render_template('hot100.html')