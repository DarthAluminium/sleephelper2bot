#sleephelperbot
import json
import requests

class WABot():
def __init__(self, json):
    self.json = json
    self.dict_messages = json['messages']
    self.APIUrl = 'https://eu108.chat-api.com/instance114187/'
    self.token = 'mjl2s79xvdjnyykc'

def send_requests(self, method, data):
    url = f"{self.APIUrl}{method}?token={self.token}"
    headers = {'Content-type': 'application/json'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    return.dict_messages
    return answer.json()

'''def show_chat_id(self,chatID):
    return self.send_message(chatID, f"Chat ID : {79870016999@c.us}")'''
