import requests

url = "https://b.zhulogic.com/designer_api/account/login_quick_pc"

data = {"phone": "13333333333",
        "code": "1111",
        "messageType": 3,
        "registration_type": 1,
        "channel": "zhulogic"}

# headers ={"Content-Type":"application/json"}

res = requests.post(url=url, json=data)

print(res.text)
