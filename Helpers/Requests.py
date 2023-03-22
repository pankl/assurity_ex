import requests


class myRequests():
    def __init__(self):
        pass
    
    def getRequest(uri):  
        return requests.get(uri, headers = {'Accept': 'application/json'})