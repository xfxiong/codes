# 通过编写程序来获取互联网上的资源
# 用程序模拟浏览器，输入一个网址，从网址中获取资源或者内容
from urllib.request import urlopen

url = 'http://www.baidu.com'
resp = urlopen(url)

with open("mybaidu.html", mode="w", encoding='utf-8') as f:
    f.write(resp.read().decode("utf-8"))  # 读取到网页的源代码
print("over!")
