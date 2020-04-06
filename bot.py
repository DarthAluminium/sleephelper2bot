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
    '''return dict_messages
    return answer.json()'''

def send_message(self, chatID, text):
    data = {"chatID" : chatID,
            "body" : text}  
    answer = self.send_requests('sendMessage', data)
    return answer
