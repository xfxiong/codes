"""
    目标：post方法
    案例:注册
    参数：
        1.json :传入json字符串
        2.headers :传入请求信息头信息
    响应：
        1.响应对象.json()
"""
import requests

url = "https://b.zhulogic.com/designer_api/account/login_quick_pc"

# headers
headers = {"Content-Type": "application/json"}

# json
data = {"phone": "13333333333",
        "code": "1111",
        "messageType": 3,
        "registration_type": 1,
        "channel": "zhulogic"}

resp = requests.post(url, json=data, headers=headers)

print(resp.status_code)
print(resp.json())
print(type(resp.json()))
# 通过键名获取值
print(resp.json()['status_code'])

print(resp.text)
print(type(resp.text))
