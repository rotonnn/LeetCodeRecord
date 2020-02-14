import requests
import json

from bs4 import BeautifulSoup
session = requests.Session()
COOKIES=None
def login():
    #登录
    url = 'https://leetcode.com'
    cookies = session.get(url).cookies
    for cookie in cookies:
        if cookie.name == 'csrftoken':
            csrftoken = cookie.value
    
    URL = 'https://leetcode-cn.com/accounts/login/'
    
    header = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "origin": "https://leetcode-cn.com",
        "referer": "https://leetcode-cn.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
        "x-requested - with": "XMLHttpRequest",
    }

    payloads = {
    'csrfmiddlewaretoken':csrftoken, 
    'login' : 'chaxinchen@gmail.com',
    'password' : 'a75124570',
    'next' : '/'
    }
    session.post(URL, data=payloads, headers=header)
    COOKIES = session.cookies


def submit():
    headers = {
        "user-agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0 .3987 .100 Safari / 537.36",
        "referer": "https://leetcode-cn.com/submissions/",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9, image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q =0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8"
    }
    sub_url = "https://leetcode-cn.com/submissions/"
    page = 1
    res = session.get(sub_url, headers=headers).content.decode('utf-8')
    soup = BeautifulSoup(res, 'html.parser')
    print(sub_url+str(page))
    sub=soup.find("tbody")
   
    print(sub)
    
    
if __name__ == "__main__":
    login()
    submit()