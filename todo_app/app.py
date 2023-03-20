from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import *
from todo_app.flask_config import Config

from flask_wtf import FlaskForm

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
@app.route('/index')
def index():
    items = get_items()
    return render_template('index.html', items=items)
    #return 'Hello World!'

@app.route('/addForm', methods=['POST'])
def addItem():
    data = request.form
    add_item(data["title"])
    return redirect(url_for('index'))
