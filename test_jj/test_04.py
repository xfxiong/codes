import requests

url = " https://hy.smartont.net:8440/web/sendMessage.do"
data = {"cellphone": "18000000202"}
headers = {
    "from": "web",
    "Ity": "0",
    "Content-Type": "application/x-www-form-urlencoded"
}
res = requests.post(url=url, data=data, headers=headers)

print(res.text)
