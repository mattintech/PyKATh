import pykath
import requests
import json

## Get ClientId from clientIds file
clientIdFile = "clientIds.json"
with open(clientIdFile, "r") as file:
    clientIds = json.load(file)

cId = clientIds['kme']

##Initialize Knox AccessToken
kat = pykath.init(kcsKeyFilePath = 'keys.json', regionalServer = 'us-kcs-api.samsungknox.com', clientId = cId)

signedClientId = kat.getSignedAccessToken()

baseUrl = "https://us-kcs-api.samsungknox.com/kcs/v1/"

def getDeviceList():
    api = baseUrl+"kme/devices/list"
    headers = {
        'Content-Type': 'application/json',
        'x-knox-apitoken': signedClientId
    }

    response = requests.get(api, headers=headers)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Request failed. Status code: {response.status_code}, Response: {response.text}")

getDeviceList()