"""
    目标：响应对象常用方法
        1.cookies
            获取响应cookie信息
        2.content
            以字节码形式获取响应信息（图片、视频..多媒体格式）
        案例：
        cookies：http://www.baidu.com
        content:http://www.baidu.com/img/bd_logo1.png?where=super
"""
import requests

url = "http://www.baidu.com"
# resp =requests.get(url)

url_img = "http://www.baidu.com/img/bd_logo1.png?where=super"
resp = requests.get(url_img)

# 获取响应cookies,字典对象
# print(resp.cookies)
# #通过键名获取响应的cookies
# print(resp.cookies['BDORZ'])

# print(resp.text) 以text文本形式解析图片---乱码

# 以字节码形式解析图片
# print(resp.content)

# 将图片写入当前目录 baidu.png
with open("../other prac/baidu.png", "wb") as f:
    f.write(resp.content)
