import requests

url = "http://47.112.144.77:9991/weather"
# 发送请求
res = requests.get(url)
# 解析响应
print(res.text)
