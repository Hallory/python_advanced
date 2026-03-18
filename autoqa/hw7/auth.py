import requests


class AuthApi:
    def __init__(self, url):
        self.url = url
        
    def login(self,username,password):
        response = requests.post(
            self.url + "/auth/login",
            json={
                "username":username,
                "password":password
            }
        )
        
        return response