# 1.拿到页面源代码  requests
# 2.通过re来提取想要的有效信息 re
import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}

resp = requests.get(url, headers=headers)
page_content = resp.text

# 解析数据

obj = re.compile(
    r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
    r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)

# 开始匹配
result = obj.finditer(page_content)
f = open("data.csv", mode='w', newline='')
csvwriter = csv.writer(f)
for i in result:
    # print(i.group('name'))
    # print(i.group('score'))
    # print(i.group('num'))
    # print(i.group('year').strip())
    dict = i.groupdict()
    dict['year'] = dict['year'].strip()
    csvwriter.writerow(dict.values())

f.close()
print('over!')
