# 拿到页面源代码
# 提取和解析数据
import requests
from lxml import etree

url = "https://guangzhou.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)
# print(resp.text)

# 解析
html = etree.HTML(resp.text)
# 拿到每一个服务商的div
divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[6]/div[1]/div')
for div in divs:
    price = div.xpath('./div/div/a[1]/div[2]/div[1]/span[1]/text()')[0].strip("¥")
    title = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))
    com_name = div.xpath('./div/div/a[2]/div[1]/p/text()')[0]
    location = div.xpath('./div/div/a[2]/div[1]/div/span/text()')[0]
    print(price)

# tree =etree.parse('b.html')
# result = tree.xpath('/html/body/ul/li')
# result = tree.xpath('/html/body/lu/li[1]/a/text()') #xpath的顺序是从1开始的
# result = tree.xpath("/html/body/div[@id='container']/div/div/span")

# ol_li_list =tree.xpath("/html/body/ol/li")
#
# for li in ol_li_list:
#     #从每个li中提取到文字信息
#     result = li.xpath("./a/text()")  #在li中继续寻找，相对查找
#     print(result)
#     result2 =li.xpath("./a/@href")   #拿到属性值：@属性
#     print(result2)
#
# print(tree.xpath("/html/body/ul/li/a/@href"))
