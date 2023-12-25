import requests
import os

def getBearerToken():
    bearerToken=None
    url = "https://us03.manage.samsungknox.com/emm/oauth/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    ## use environment varaibles instead of hard coding credentails
    # example export apiuser="apiuser@domain.com"
    data = {
        "grant_type": "client_credentials",
        "client_id": os.environ.get('apiuser'),
        "client_secret": os.environ.get('apipass')
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        responseDict=response.json()
        bearerToken=responseDict['access_token']
    else:
        print(f"Request failed. Status code: {response.status_code}, Response: {response.text}")
    return bearerToken


def getDeviceList(bearerToken):
    getDevicesUrl = "https://us03.manage.samsungknox.com/emm/oapi/device/selectDeviceList"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"bearer {bearerToken}"
    }

    data = {
        "deviceStatus": "A"
    }

    response = requests.post(getDevicesUrl, headers=headers, data=data)
    print(response.status_code)
    print(response.json())

token=getBearerToken()

getDeviceList(token)