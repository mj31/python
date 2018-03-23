import requests
params = {"action":"getMediaIdByProviderBookId","providerCode":"ownPublish","providerBookId":90275}
result = requests.post("http://10.4.37.32/media/api.go",data=params)
print(result.text)



