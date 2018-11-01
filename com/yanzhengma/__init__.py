import requests
url='http://101.201.109.144:6161/fytv/cms?ac=videolist&ids=2180,2181'

rep = requests.get(url)
rep.encoding = 'utf-8'
print(rep.content)