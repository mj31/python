import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Referer':'http://dangdu.dangdang.com',
    'Accept':'application/javascript, */*;q=0.8',
    'Host':'dangdu.dangdang.com',
}
payloadR = {"bookId":105821}
payloadT = {"bookId":90138}
rows = int(5000)
for i in range(0, rows):
    r = requests.get("http://dangdu.dangdang.com/book/click/ajaxBookClick.shtml",params=payloadR,headers = headers)
    print("r==="+r.text)
    t = requests.get("http://dangdu.dangdang.com/book/click/ajaxBookClick.shtml",params=payloadT,headers = headers)
    print("t==="+t.text)
