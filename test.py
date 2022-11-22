import requests

URL = 'https://api.twitch.tv/helix/streams?user_login=xqc'
authURL = 'https://id.twitch.tv/oauth2/token'
Client_ID = ''
Secret  = ''

AuthParams = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }


def Check():
    AutCall = requests.post(url=authURL, params=AuthParams)
    access_token = AutCall.json()['access_token']

    head = {
    'Client-ID' : Client_ID,
    'Authorization' :  "Bearer " + access_token
    }

    json_info = requests.get(URL, headers = head).json()
    
    return access_token


