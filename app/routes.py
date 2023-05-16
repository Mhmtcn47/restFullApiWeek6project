from flask import render_template

from app import app

@app.route('/')
def home():
    marvel= {
    'instruction':('play1', 'play2')
    }
    return render_template('index.jinja',title='home', instruction=marvel['instruction'])



@app.route('/signin')
def signin():

    return render_template('index.jinja')



@app.route('/register')
def register():

    return render_template('index.jinja')