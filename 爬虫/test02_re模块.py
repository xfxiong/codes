import re

# #findall :匹配字符串中的所有符合正则的内容,返回列表
# lst =re.findall(r"\d+","我的电话是：10086，他的电话是：10010")
# print(lst)   #['10086', '10010']
#
# #finditer :匹配字符串中的所有内容【返回的是迭代器】，从迭代器中拿到内容需要.group()
# it =re.finditer(r"\d+","我的电话是：10086，他的电话是：10010")
# for i in it:
#     print(i.group())
# #10086
# #10010
#
# #search,找到一个结果就返回，返回的结果是match对象，拿数据需要.group()
# s =re.search(r"\d+","我的电话是：10086，他的电话是：10010")
# print(s.group())
# #10086
#
# #match 是从头开始匹配的，如果开头不是需要的内容（数字），报错，其他是全文匹配
# s1 =re.match(r"\d+","10086，他的电话是：10010")
# print(s1.group())  #10086

# #预加载正则表达式
# obj =re.compile(r"\d+")
# ret =obj.finditer("我的电话是：10086，他的电话是：10010")
# for i in ret:
#     print(i.group())
#
# s = obj.findall("a，我就不信你不还10000000")
# print(s)  #['10000000']

s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jolin'><span id='2'>宋媞</span></div>
<div class='jj'><span id='3'>大聪明</span></div>
<div class='jimy'><span id='4'>凡凡</span></div>
<div class='tory'><span id='5'>火箭哥</span></div>
"""

# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)
# re.S 让.能匹配换行符
result = obj.finditer(s)
for i in result:
    print(i.group("name"))
    print(i.group("id"))
