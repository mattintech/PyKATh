## Tutorial for authentication can be found here: https://docs.samsungknox.com/dev/knox-cloud-authentication/tutorial/tutorial-for-customers-generate-access-token/

import pyktl
import json
import requests


def loadCertificateFile(path):
    kcsKeysFile = "keys.json"
    with open(kcsKeysFile, "r") as file:
        kcsCert = json.load(file)

publicKey = kcsCert['Public']

def generateSignClientID(clientId):
    signedClientId = pyktl.generate_signed_client_identifier_jwt(kcsKeysFile, clientId)
    return signedClientId

def generateAccessToken(signedClientId):
    accessToken=None
    url = "https://us-kcs-api.samsungknox.com/ams/v1/users/accesstoken" ## make sure to leverage the correct URL for your region
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "clientIdentifierJwt": signedClientId,
        "base64EncodedStringPublicKey": publicKey,
        "validityForAccessTokenInMinutes": 30
        }
    
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        responseDict=response.json()
        accessToken=responseDict['accessToken']
    else:
        print(f"Request failed. Status code: {response.status_code}, Response: {response.text}")
    return accessToken

def generateSignedAccessToken(accessToken):
    result=pyktl.generate_signed_access_token_jwt(kcsKeysFile, accessToken)
    return result

def getAccessToken(clientId):
    signedClientId=generateSignClientID(clientId)
    accessToken=generateAccessToken(signedClientId)
    signedAccessToken=generateSignedAccessToken(accessToken)
    return signedAccessToken