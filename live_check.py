import requests
import webbrowser
from twitch_app import *

def Check(streamer):
    url = f'https://api.twitch.tv/helix/streams?user_login={streamer}'
    authURL = 'https://id.twitch.tv/oauth2/token'
    Client_ID = ''
    Secret  = ''

    AuthParams = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }

    AutCall = requests.post(url=authURL, params=AuthParams)
    access_token = AutCall.json()['access_token']

    head = {
    'Client-ID' : Client_ID,
    'Authorization' :  "Bearer " + access_token
    }


    json_info = requests.get(url, headers = head).json()['data']
    print(json_info)
    if json_info:
        json_info = json_info[0]
        if json_info['type'] == 'live':
            return True
        else:
            return False
    else:
        return False


def streamer_name(streamer):
    url = f'https://api.twitch.tv/helix/streams?user_login={streamer}'
    authURL = 'https://id.twitch.tv/oauth2/token'
    Client_ID = ''
    Secret  = ''

    AuthParams = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }

    AutCall = requests.post(url=authURL, params=AuthParams)
    access_token = AutCall.json()['access_token']

    head = {
    'Client-ID' : Client_ID,
    'Authorization' :  "Bearer " + access_token
    }

    try:
        json_name = requests.get(url, headers = head).json()['data']
        json_n = json_name[0]
    
        streamer_name_return = json_n['user_name']
        print(streamer_name_return)
        return str(streamer_name_return)
    except IndexError:
        return False


def go_to_stream(streamername):
        webbrowser.open_new(f'https://www.twitch.tv/{streamername}')



def Long_Check(hour, streamer, checked):
    import time
    url = f'https://api.twitch.tv/helix/streams?user_login={streamer}'
    authURL = 'https://id.twitch.tv/oauth2/token'
    Client_ID = ''
    Secret  = ''

    AuthParams = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }

    AutCall = requests.post(url=authURL, params=AuthParams)
    access_token = AutCall.json()['access_token']

    head = {
    'Client-ID' : Client_ID,
    'Authorization' :  "Bearer " + access_token
    }

    if hour == "00" and checked == "off":
        while True:
            requested = Check(streamer)
            if requested == True:
                webbrowser.open_new(f'https://www.twitch.tv/{streamer}')
                return False
            else:
                print("working...")
                time.sleep(60)
            continue
    elif hour == "00" and checked == "on":
        while True:
            requested = Check(streamer)
            if requested == True:
                return True
            else:
                print("working unchecked")
                time.sleep(60)
            continue
    elif hour != "00" and checked == "off":
        hour = int(hour)*3600
        while hour < 0:
            print(hour)
            requested = Check(streamer)
            if requested == True:
                webbrowser.open_new(f'https://www.twitch.tv/{streamer}')
                return False
            elif hour == 0:
                return False
            else:
                print(f"{hour} unchecked")
                time.sleep(60)
                hour = hour - 60
                continue
    elif hour != "00" and checked == "on":
        hour = int(hour)*3600
        while hour <= 0:
            requested = Check(streamer)
            if requested == True:
                return True
            if hour == 0:
                return False
            else:
                print(f"{hour} checked")
                time.sleep(60)
                hour = hour - 60
                continue
