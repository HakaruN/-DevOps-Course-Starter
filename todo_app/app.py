from flask import Flask, render_template, request, redirect, url_for
from .data.trello_items import *
from todo_app.flask_config import Config

import os


from flask_wtf import FlaskForm

app = Flask(__name__)
app.config.from_object(Config())

boardID = "645106104aeafb96fe026623"
todoID = "6451065f9818f6f58c290efb"
doneID = "64f1e683328cb18730751208"

@app.route('/')
@app.route('/index')
def index():    
    return render_template('index.html', boardID=boardID, todoID=todoID, doneID=doneID, todo=get_Cards_By_List(todoID), done=get_Cards_By_List(doneID))

@app.route('/addCard', methods=['POST'])
def addItem():
    data = request.form
    add_Card(boardID, todoID, data["name"], data["description"])
    return redirect(url_for('index'))

@app.route('/deleteCard', methods=['POST'])
def delItem():
    data = request.form
    return redirect(url_for('index'))

@app.route('/deleteCards', methods=['POST'])
def delAllItems():    
    clear_Cards_By_Board(boardID)
    return redirect(url_for('index'))

@app.route('/changeDone', methods=['POST', 'GET'])
def changeStatusByID():
    change_List_By_ID(boardID, "asd", doneID)
    return redirect(url_for('index'))

@app.route('/changeTodo', methods=['POST', 'GET'])
def changeStatusByName():
    args = request.args.to_dict()
    print(args)
    cardName = args['name']
    cardDest = args['status']
    print("Card name: " + cardName + ", card dest: " + cardDest)
    change_List_By_Name(boardID, cardName, cardDest)
    return redirect(url_for('index'))