# 列表嵌套
clname_list = [['Tom', 'Wendy'], ['张三', '李四', '王五'], ['小明', '小文', '小红']]
print(clname_list)
print(clname_list[1])
print(clname_list[1][1])

# 打印列表中的所有数据
print("1.使用while循环遍历列表——————")
name_list = ['Tom', 'Wendy', 'David', 'Andy', 'Lily']
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

print("2.使用for循环遍历列表——————")
for i in name_list:
    print(i)
