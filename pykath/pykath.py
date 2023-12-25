import pyktl
import json
import requests

class init:
    def __init__(self, kcsKeyFilePath, regionalServer, clientId):
        print("Init Class")
        self.regionalServer = regionalServer
        self.kcsKeyFilePath = kcsKeyFilePath
        self.clientId = clientId

    def getPublicKeyFromKeysFile(self):
        with open(self.kcsKeyFilePath, "r") as file:
            kcsCert = json.load(file)
            global publicKey 
            publicKey = kcsCert['Public']
            
    def generateSignClientID(self):
        signedClientId = pyktl.generate_signed_client_identifier_jwt(self.kcsKeyFilePath, self.clientId)
        return signedClientId

    ## Improve method error detection 
    ## todo add proxy support
    def generateAccessToken(self, signedClientId):
        accessToken=None
        url = f"https://{self.regionalServer}/ams/v1/users/accesstoken" ## make sure to leverage the correct URL for your region
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

    def generateSignedAccessToken(self, accessToken):
        result=pyktl.generate_signed_access_token_jwt(self.kcsKeyFilePath, accessToken)
        return result

    def getSignedAccessToken(self):
        self.getPublicKeyFromKeysFile()
        signedClientId=self.generateSignClientID()
        accessToken=self.generateAccessToken(signedClientId)
        signedAccessToken=self.generateSignedAccessToken(accessToken)
        return signedAccessToken