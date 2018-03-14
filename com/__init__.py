import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Referer':'http://dangdu.dangdang.com/book/82607.shtml',
    'Accept':'application/javascript, */*;q=0.8',
    'Host':'dangdu.dangdang.com',
}
payload = {"bookId":82607}
rows = int(10)
for i in range(0, rows):
    r = requests.get("http://dangdu.dangdang.com/book/click/ajaxBookClick.shtml",payload,headers = headers)
    print(r.text)