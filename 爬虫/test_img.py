import requests
from bs4 import BeautifulSoup

url = "http://www.netbian.com/weimei/"
domain = "http://www.netbian.com"
resp = requests.get(url)
resp.encoding = 'gbk'
# print(resp.text)

page = BeautifulSoup(resp.text, "html.parser")
imgic = page.find("a", title="秋天的梦 梦幻之秋 山 树 河流 日落唯美壁纸 更新时间：2020-10-28")

# print(imgic)
img = imgic.find('img')
src = img.get('src')
# 下载图片
img_resp = requests.get(src)
# print(img_resp.content)  #拿到字节
img_name = src.split("/")[-1]  # 拿到url最后一个/以后的内容
with open("img/" + img_name, "wb") as f:
    f.write(img_resp.content)  # 图片内容写入文件

    f.close()
    print("over", img_name)
