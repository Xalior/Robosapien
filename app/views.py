from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    state = {'summary': 'Norman'}  # fake user
    return render_template('index.html',
                           title='Ready&hellip;',
                           state=state)
