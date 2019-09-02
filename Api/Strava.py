import requests
import json

class strava:

    def __init__(self):
        self.perPage = 200 # Integer | Numero de pacote de dados

        self.client_id = 37249
        self.client_secret = 'f8ec88693e0e5f658dd8adbb0bd2e4742b1b1685'
        self.code = 'eef2d68aad13fe2d6bdbdd20f2be4b62a5501237'
        self.grant_type = 'authorization_code'


    def getPedal(self, token):

        token = 'Bearer ' + token

        response = requests.get( 'https://www.strava.com/api/v3/athlete/activities?per_page=' + str(self.perPage), headers={'Authorization':token})
        json_response = response.json()
        return json_response


    def postToken(self):
        self.url = "https://www.strava.com/oauth/token"

        response = requests.post("https://www.strava.com/oauth/token", data={'client_id': self.client_id, 'client_secret': self.client_secret, 'code': self.code, 'grant_type': self.grant_type})
        json_response = response.json()
        retorno = json_response['access_token']
        return retorno



