from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import surveys


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

app.debug = True

debug = DebugToolbarExtension(app)

responses =[]

@app.route('/')
def get_root():
    return render_template('/home')