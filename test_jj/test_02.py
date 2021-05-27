import requests

url = "http://47.112.144.77:9991/address"
# 设置参数
params = {"phoneNum": "18600000000"}
# 发送请求
res = requests.get(url, params=params)
# 解析响应
print(res.text)
