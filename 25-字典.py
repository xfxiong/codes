dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)
for item in dict1.items():
    print(item)

for key, value in dict1.items():
    print(f'{key}={value}')

# 函数 1.get()
print(dict1.get('name'))
print(dict1.get('id'))  # 不存在返回None
print(dict1.get('id', 'lily'))

# 2.keys()  查找字典中的所有key，返回可迭代对象
print(dict1.keys())

# 3.values()  查找字典中的所有值，返回可迭代对象
print(dict1.values())

# 4.items()  查找字典中的所有键值对，返回可迭代对象，里面的元素是元组
print(dict1.items())
# 结果：dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])


print(dict1['name'])  # 存在key，返回对应值
# print(dict1['id'])   #不存在，报错

dict1['age'] = 22  # 增加、修改
dict1['name'] = 'Andy'
print(dict1)

# del()  del  删除字典或指定键值对
# del(dict1)
# print(dict1)

# del dict1['name']
del (dict1['name'])
print(dict1)
# clear() 清空字典
dict1.clear()
print(dict1)
