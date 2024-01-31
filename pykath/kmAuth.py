import requests
import json
import os


kmConfigFile = "kmCreds.json"
def getBearerToken():
    with open(kmConfigFile, 'r') as file:
        kmApiConfig = json.load(file)
    
    ## put logic for json validation
    server = kmApiConfig['kmServer']
    apiUser = kmApiConfig['apiUser']
    apiPass = kmApiConfig['apiPass']

    bearerToken=None
    url = f"https://{server}/emm/oauth/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials",
        "client_id": apiUser,
        "client_secret": apiPass
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