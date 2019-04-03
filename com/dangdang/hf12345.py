import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Referer':'hf12345.vip',
    'Accept':'application/javascript, */*;q=0.8',
    'Host':'hf12345.vip',
}
payloadT = {"id":19031988080086,"isSearchPassWord":"22ca613f5555571f5e","tag":"91959a45556a02","sys_random":0.5853395519307}
#2:onclick="detail('19031988080086','5f6b4f24065f041e4357','53174353e0777c7a08')
#1:detail('19031988080086','5f6b4f24065f041e4357','53174353e0777c7a08');
rows = int(800)
for i in range(0, rows):
    r = requests.get("http://hf12345.vip/public/mhwz/todetail",params=payloadT,headers = headers)
