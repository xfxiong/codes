# 登录 ->得到cookie
# 带着cookie 去请求到书架url --书架上的内容
# 必须得把上面两个操作连起来
# 我们可以使用session进行请求 -->session可以认为是一连串的请求，在这个过程中的cookie不会丢失

import requests

# 会话
session = requests.session()
data = {
    "loginName": "13249704047",
    "password": "xxf123456"
}

# 1.登录
url = "https://passport.17k.com/ck/user/login"

resp = session.post(url, data=data, verify=False)
# print(resp.text)
print(resp.cookies)

# 2.拿书架的数据
# 刚才那个session中有cookie
resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(resp.json())
