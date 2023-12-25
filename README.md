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

## Prerequesits 

```
pip install PyKATh requests
```

## Getting Started
```
## Initialize the Knox Token Library 
kat = knox_common.KnoxAccessToken(kcsKeyFilePath = 'keys.json', regionalServer = 'us-kcs-api.samsungknox.com', clientId = cId)
signedKCSToken = kat.getSignedAccessToken()
print(signedKCSToken) ## Use this balue in the 'x-knox-apitoken' header to call most KCSAPis (for 30mins) in the

```

## API Requests
I am currently taking requests to build examples in python.  If there is something you would like to see please click on the link below and log a feature request.
[New Feature Here](https://github.com/mattintech/KnoxAccessToken-python/issues/new)

Please make sure to add the label 'enhancement' and try and be as detailed as possible.  Provide examples where possible. 

## Docs
TODO

