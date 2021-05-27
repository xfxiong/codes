"""
    目标：Get请求方法
    案例:http://www.baidu.com
    请求：
        1.请求方法：Get
    响应：
        1.响应对象.url  #获取请求url
        2.响应对象.status_code  #获取响应状态码
        3.响应对象.text  #以文本形式显示响应内容
"""

# 1.导包
import requests

# 2.调用get
url = "http://www.baidu.com"
resp = requests.get(url)

# 3.获取请求url
print("请求url：", resp.url)

# 4.获取响应状态码
print("状态码：", resp.status_code)

# 5.以文本形式显示响应内容
print("文本响应内容：", resp.text)
