import requests
import json



############Boards###############
def get_boards():
    url = "https://trello.com/1/members/me/boards"
    query = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6"}
    #r = requests.get("https://trello.com/1/members/me/boards", params=payload)
    #r_dict = r.json()
    return sendRequest("GET", url, headers=None, query=query)


################################


###########lists################
def get_lists(boardID):
    url = "https://api.trello.com/1/boards/" + boardID + "/lists"
    query = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6"}
    headers = {"Accept": "application/json"}
    return sendRequest("GET", url, headers=headers, query=query)


def get_list(listID):
    url = "https://api.trello.com/1/lists/" + listID
    query = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6", 'cards' : "all"}
    return sendRequest("GET", url, headers=None, query=query)

################################



###########cards################
def get_Cards_By_Board(boardID):
    url = "https://api.trello.com/1/boards/" + boardID + "/cards"
    query = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6"}
    return sendRequest("GET", url, headers=None, query=query)


def get_Cards_By_List(listID):
    url = "https://api.trello.com/1/lists/" + listID + "/cards"
    headers = {"Accept": "application/json"}
    query = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6"}
    return sendRequest("GET", url, headers, query)


def clear_Cards_By_Board(boardID):
    cards = get_Cards_By_Board(boardID)
    for card in cards:
        print("Card ID: " + card['id'] + ", name: " + card['name'])
        delete_Card(card['id'])


def clear_Cards_By_List(listID):
    cards = get_Cards_By_List(listID)
    for card in cards:
        delete_Card(card['id'])


def delete_Card(cardID):
    url = "https://api.trello.com/1/cards/" + cardID
    query = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6"}
    return sendRequest("DELETE", url, headers=None, query=query)


def add_Card(boardID, listID, cardName, cardDescription):
    url = "https://api.trello.com/1/cards"
    headers = {"Accept": "application/json"}
    query = {'idList': listID, 'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6",'name' : cardName
    , 'desc': cardDescription}
    return sendRequest("POST", url, headers, query)


def change_List_By_ID(boardID, cardID, listID):
    cards = get_Cards_By_Board(boardID)
    headers = {"Accept": "application/json"}
    query = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6", 'idList' : listID}
    url = "https://trello.com/1/cards/" + cardID
    return sendRequest("PUT", url, headers=headers, query=query)
    

def change_List_By_Name(boardID, cardName, listID):
    cards = get_Cards_By_Board(boardID)
    headers = {"Accept": "application/json"}
    for card in cards:
        if card['name'] == cardName:
            query = {'key': "45423e137951812569d019961fb403c2", 'token' : "ATTA2b3a7034386c06e9d26162ffd749f17a2cb130a57bbbd92c4e08bbb59a85efa3023E78E6", 'idList' : listID}
            url = "https://trello.com/1/cards/" + card['id']
            return sendRequest("PUT", url, headers=headers, query=query)

##############helper functions###############
def sendRequest(reqType ,url, headers, query):
    r = requests.request(reqType, url, headers= (headers if headers != None else None), params=query)
    return r.json()

#############################################