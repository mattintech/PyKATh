import KnoxAccessToken as kat
import requests
import json



clientIdFile = "clientId.json"
with open(clientIdFile, "r") as file:
    clientIds = json.load(file)

clientId = clientIds['kme']
signedClientId = kat.getAccessToken(clientId)

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