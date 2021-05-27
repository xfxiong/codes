# 1.定位到2021必看片
# 2.从2021必看片中提取到子页面的链接地址
# 3.请求子页面的链接地址，拿到我们想要的下载地址
import requests
import re

domain = 'https://dytt89.com/'

resp = requests.get(domain, verify=False)  # verify=False，去掉安全验证
resp.encoding = 'gb2312'  # 指定字符集
# print(resp.text)

obj = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj1 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj2 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td '
                  r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

result = obj.finditer(resp.text)
child_href_list = []
for i in result:
    ul = i.group('ul')
    # print(ul)

    # 提取子页面链接

    result2 = obj1.finditer(ul)
    for j in result2:
        child_href = domain + j.group('href').strip('/')
        child_href_list.append(child_href)  # 保存子链接页面

# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312'
    result3 = obj2.search(child_resp.text)
    print(result3.group('movie'))
    print(result3.group('download'))
    # print(child_resp.text)
    # break    #测试用
