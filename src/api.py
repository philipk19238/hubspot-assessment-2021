import os
import requests


class APIHelper:

    def __init__(self, api_key=None):
        self.API_KEY = api_key
        self.session = requests.Session()
        self.headers = {'Authorization': f"Bearer {self.API_KEY}"}

    def get(self, endpoint):
        resp = self.session.get(endpoint, headers=self.headers)
        return resp

    def post(self, endpoint, **kwargs):
        resp = self.session.post(endpoint, headers=self.headers, **kwargs)
        return resp
