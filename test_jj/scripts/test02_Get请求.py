"""
    目标：Get请求方法带参数
    案例:
        1.http://www.baidu.com?id=1001
        2.http://www.baidu.com?id=1001,1002
        3.http://www.baidu.com?id=1001&kw=北京
    请求：
        1.请求方法：Get
    参数：
        params:字典或字符串（推荐使用字典）
    响应：
        1.响应对象.url  #获取请求url
        2.响应对象.status_code  #获取响应状态码
        3.响应对象.text  #以文本形式显示响应内容
"""

# 1.导包
import requests

# 2.调用get
url = "http://www.baidu.com"
# 不推荐写法  静态 url ="http://www.baidu.com?id=1001"
# 不推荐 字符串形式 resp=requests.get(url,params="id=1001")
# 案例1：定义字典
# params ={"id":1001}

# 案例2:
# params={"id":[1001,1002]} #不推荐
# params={"id":"1001,1002"}

# 案例3
params = {"id": 1001, "kw": "北京"}

resp = requests.get(url, params=params)

# 3.获取请求url
print("请求url：", resp.url)

# 4.获取响应状态码
print("状态码：", resp.status_code)

# 5.以文本形式显示响应内容
# print("文本响应内容：",resp.text)
