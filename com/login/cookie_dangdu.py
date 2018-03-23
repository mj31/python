import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录后才能访问的网页
url = 'http://dangdu.dangdang.com/author/book/list'

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'JSESSIONID=174E3ECB4247827C49ADA1DD1EA0E0C0; __permanent_id=20171207155849592112071965762413637; permanent_key=20171208163018130647999867e8b70b; ddUserFirstToRead=yes; pageNum=1960151877%3A1; readType=2; ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; JSESSIONID=E5AE2EFA6EF28E2DDD5D755C9CFFDC65; __ddclick_visit=0000000001.1; out_refer=%7C; LOGIN_TIME=1513050870112; login.dangdang.com=.AYH=2017121211461212124596382&.ASPXAUTH=dzl1QIZCOze07y4VTE8s0zfu7fBK/T1g; dangdang.com=email=bWFzb25nQGRhbmdkYW5nLmNvbQ==&nickname=&display_id=9866107529956&customerid=lV13Y6ANP2Bp4cKTmMjclA==&viptype=Uyfz+Ya7Sf4=&show_name=masong; ddoy=email=masong%40dangdang.com&nickname=&agree_date=1&validatedflag=2&uname=masong%40dangdang.com&utype=0&.ALFG=on&.ALTM=1513050999; sessionID=pc_a3a25c4647b771c7a5f1ae9b3eec26226b247c099943b4be507111d9cebc7831; __dd_token_id=201712121156392250831088727b7222; __rpm=login_page.login_password_div..1513050998571%7Clogin_mobile_bind_page...1513051000548; utoken=159605918#43f466d7c87d7aa3bf497efcbd8ad2b6; __visit_id=20171212115339010117478935569116213; __out_refer=; __trace_id=20171212115651821284792148319239727'

#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

# 设置请求头
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

# 在发送get请求时带上请求头和cookies
resp = requests.get(url, headers=headers, cookies=cookies)

print(resp.content.decode('utf-8'))