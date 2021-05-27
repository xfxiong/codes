# 1.拿到主页面的源代码，然后提取子页面的链接地址，href
# 2.通过href拿到子页面的内容，从子页面中找到图片的下载地址 img-src
# 3.下载图片
import time

import requests
from bs4 import BeautifulSoup

url = "http://www.netbian.com/weimei/"
domain = "http://www.netbian.com"
resp = requests.get(url)
resp.encoding = 'gbk'
# print(resp.text)

page = BeautifulSoup(resp.text, "html.parser")
alist = page.find("div", class_='list').find_all("a")
# print(alist)
alist.pop(2)
alist.pop(2)

for a in alist:
    href = domain + a.get('href')  # 通过get属性值
    # 拿到子页面源代码
    print(href)
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'gbk'
    child_page_text = child_page_resp.text
    # print(child_page_text)
    child_page = BeautifulSoup(child_page_text, "html.parser")
    div = child_page.find("div", class_='pic')
    img = div.find('img')
    src = img.get('src')
    print(src)
    # 下载图片
    img_resp = requests.get(src)
    # print(img_resp.content)  #拿到字节
    img_name = src.split("/")[-1]  # 拿到url最后一个/以后的内容
    with open("img/" + img_name, mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件

        print("over", img_name)
        f.close()
        time.sleep(3)
