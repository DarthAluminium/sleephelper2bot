#sleephelperbot
import json
import requests
import datetime

class WABot():
def __init__(self, json):
    self.json = json
    self.dict_messages = json['messages']
    self.APIUrl = 'https://eu108.chat-api.com/instance114187/'
    self.token = 'mjl2s79xvdjnyykc'
def show_chat_id(self,chatID):
    return self.send_message(chatID, f"Chat ID : {chatID}")