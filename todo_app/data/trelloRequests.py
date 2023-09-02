import requests


##TODO list ID: 6451065f9818f6f58c290efb
##main endpoint: https://trello.com/1/boards

##TODO:
#Get boards
#Get Cards
#Add cards to board
boardID = "645106104aeafb96fe026623"

def get_boards():
    payload = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6"}
    r = requests.get("https://trello.com/1/members/me/boards", params=payload)
    r_dict = r.json()


def get_Cards(boardID):
    payload = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6"}
    r = requests.get('https://api.trello.com/1/boards/' + boardID + '/cards', params=payload)
    r_dict = r.json()
    print(r_dict[0]["name"])
    return r_dict


def clear_Cards(boardID):
    payload = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6"}
    cards = getCards(boardID)
    for card in cards:
        r = requests.request("DELETE",'https://api.trello.com/1/cards/' + card['id'], params=payload)


def add_Card(boardID, cardName):
    payload = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6",
    'idList' : "6451065f9818f6f58c290efb", 'name' : cardName
    }
    r = requests.request("POST",'https://trello.com/1/cards', params=payload)


#get_boards()
#get_cards(boardID)
#addCard(boardID, "NewCard")
#clearCards(boardID)