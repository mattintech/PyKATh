[![BuildStatus](https://github.com/mattintech/PyKATh/workflows/CI/badge.svg)](https://github.com/mattintech/PyKATh/actions/workflows/auto-build-publish.yml)
[![PyPI Version](https://img.shields.io/pypi/v/PyKATh.svg)](https://pypi.org/project/PyKATh/)
[![Active branch](https://img.shields.io/badge/branch-master-lightgrey.svg)](https://github.com/mattintech/PyKATh/tree/master/)


<div style="text-align: right"> 
    <a href="https://www.buymeacoffee.com/mattintech" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</div>

# Python Knox Access token - Helper (PyKATh)

**This is not an offical Samsung library or repository**

A colleciton of python code that assists in the creation of a signed access token to be used with the Samsung Knox Cloud Service 'KCS' APIs.  
For more information on the flow of Samsung's Knox Cloud Authentication API - see their tutorial here: (https://docs.samsungknox.com/dev/knox-cloud-authentication/tutorial/tutorial-for-customers-generate-access-token/)


## Currently supported KCS APIs

This library can generate signed Tokens for the following Samsung KC Services:
- Knox Mobile Enrollment ('KME')
- Knox Conifgure ('KC')
- Knox E-FOTA ('KE1')
- Knox Asset Intelligence ('KAI')
- Knox Guard ('KG')
- Knox Deployment Program ('KDP')

Todo
- Knox Manage ('KM') is currently not supported, but work is in progress.

## Prerequesits 

```
pip install PyKATh requests
```

## Getting Started
```
## Initialize the Knox Token Library. 
kat = knox_common.KnoxAccessToken(kcsKeyFilePath = 'keys.json', regionalServer = 'us-kcs-api.samsungknox.com', clientId = cId)

## request a signed token for a specific KCS ClientId.
signedKCSToken = kat.getSignedAccessToken()

## Use this balue in the 'x-knox-apitoken' header to call most KCSAPis (for 30mins) in the
print(signedKCSToken) 
```

## TODO
- docs
- KM API Helper
- create API examples for each service

