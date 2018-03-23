from bs4 import BeautifulSoup
import requests
import random
import json

url = "http://music.163.com/weapi/v3/playlist/detail"
header={
    'Accept':'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/59.0',
    'Host':'music.163.com',
    'Referer':'http://music.163.com/'
}

params={"params":"7HRlh26MC9E3aYx0IgSTwNlMTz9V+ZUL8QbLddvDy+8fhWhfdTk31qz0mUVpgiTS"
        ,"encSecKey":"40c484d28f41d2465b1a9237c05e82cba7ecd7aaf3ac0deb4c244b9f74856a992c69adfc774207ea588c3b4abfec891858f2ce54a38a231fe741dc3ba9a64e95c600928712b5e07eb1ae34b4d8877e52c255125c184417f53028463ca5e998a6b70b6699f9e075f7d6483b3e12019de977be56301b02d37110d8662727d99d08"}

timeout = random.choice(range(80, 180))
content = requests.post(url,data=params)
print(content.content)
#print(content.text.replace("\'","\""))
#json = json.dumps(content.text)
#print(json)

