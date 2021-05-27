# 代理原理：通过第三方的一个机器去发送请求

import requests

# 111.177.192.8
proxies = {
    "https": "https://111.177.192.8"
}

resp = requests.get("https://www.baidu.com")

resp.encoding = 'utf-8'
print(resp.text)
