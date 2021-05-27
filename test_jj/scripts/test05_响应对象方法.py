"""
    目标：响应对象常用方法
        1.encoding
            获取请求编码
            设置响应编码
        2.headers
            获取响应信息头信息
        案例：http://www.baidu.com
"""
import requests

url = "http://www.baidu.com"
resp = requests.get(url)

# 查看默认请求编码 ISO-8859-1
print(resp.encoding)

# 设置响应编码
resp.encoding = 'utf-8'

print(resp.text)

# 查看响应信息头
print(resp.headers)  # 比较重要，项目工作中，一般服务器返回的token、session都在headers中
