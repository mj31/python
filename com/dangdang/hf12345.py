import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Referer':'hf12345.vip',
    'Accept':'application/javascript, */*;q=0.8',
    'Host':'hf12345.vip',
}
payloadT = {"id":19032988100058,"isSearchPassWord":"2c7c3628292157","tag":"91959a45556a02","sys_random":0.5853395519307}
#2:onclick="detail('19031988080086','5f6b4f24065f041e4357','53174353e0777c7a08')
#1:detail('19031988080086','5f6b4f24065f041e4357','53174353e0777c7a08');
rows = int(1000)
for i in range(0, rows):
    r = requests.get("http://hf12345.vip/public/mhwz/todetail",params=payloadT,headers = headers)
