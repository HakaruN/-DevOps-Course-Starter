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
    cardsTodo = []
    for c in get_Cards_By_List(todoID):
        cardsTodo.append(Card(c['id'], c['name'], c['desc']))

    cardsDone = []
    for c in get_Cards_By_List(doneID):
        cardsDone.append(Card(c['id'], c['name'], c['desc']))

    #return render_template('index.html', boardID=boardID, todoID=todoID, doneID=doneID, todo=get_Cards_By_List(todoID), done=get_Cards_By_List(doneID))
    return render_template('index.html', boardID=boardID, todoID=todoID, doneID=doneID, todo=cardsTodo, done=cardsDone)

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


@app.route('/changeTodo', methods=['POST', 'GET'])
def changeStatus():
    args = request.args.to_dict()
    card = Card(args['id'], args['name'], args['desc'])
    cardDest = args['status']
    change_List(boardID, card, cardDest)
    return redirect(url_for('index'))