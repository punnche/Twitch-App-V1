import requests

def check_if_online():
    website_url = "https://status.twitch.tv/"
    status = {
        200: "Available",
        301: "Permanent Redirect",
        302: "Temporary Redirect",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable"
    }

    res = requests.get(website_url)
    if status[res.status_code] == 'Available':
        return True
    else:
        return False



class Online:
    import requests
    def __init__(self):
        self.WEBSITE_URL = "https://status.twitch.tv/"
        self.status = {
            200: "Available",
            301: "Permanent Redirect",
            302: "Temporary Redirect",
            404: "Not Found",
            500: "Internal Server Error",
            503: "Service Unavailable"
        }

        self.verify = self.requests.get(self.WEBSITE_URL)
        self.code = self.status[self.verify.status_code]

def run():
    return Online()

