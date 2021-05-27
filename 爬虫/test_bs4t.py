# 安装 pip install bs4
# 1.拿到页面源代码
# 2.使用bs4进行解析，获取数据
import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
# print(resp.text)

f = open("菜价.csv", mode="w", newline='', encoding='utf-8')
csvwriter = csv.writer(f)

# 解析数据
# 1.源代码交给beautifulsoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
# 2.从bs中查找数据
# find(标签，属性=‘属性值’)
# find_all()
table = page.find("table", class_="hq_table")  # class是python的关键字,加上下划线
# table =page.find("table",attrs={"class":"hq_table"})  #和上面那个同一个意思避免class
# print(table)

# 拿到所有数据行
trs = table.find_all('tr')[1:]  # tr找行;td列
for tr in trs:
    tds = tr.find_all("td")  # 每行中的所有td
    name = tds[0].text  # .text 拿到被标签标记的内容
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    date = tds[6].text
    # print(name,low,avg,high,gui,kind,date)
    csvwriter.writerow([name, low, avg, high, gui, kind, date])

f.close()
print("over!")
