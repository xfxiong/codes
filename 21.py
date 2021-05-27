my_list = ['lily', 'Tom', 'Rose']

print(my_list)
print(my_list[0])
# index() 查找
print(my_list.index('lily'))
print(my_list.index('Tom'))
# count() 数据在列表中出现的次数
print(my_list.count('lily'))

# len() 长度，列表中数据的个数
print(len(my_list))

# in
print('Tom' in my_list)
print('lily' not in my_list)

# append()
my_list.append('Andy')
print(my_list)
my_list.append([11, 22])
print(my_list)

my_list.extend('Wendy')
print(my_list)
my_list.extend(['xiaoming', 'xiaohong'])
print(my_list)

my_list.insert(1, 'David')
print(my_list)

# #体验案例：查找用户输入的名字是否存在
# name_list =['Tom','Wendy','Lily','Andy']
#
# name = input("输入一个名字：")
#
# if name in name_list:
#     print(f"你输入的名字{name},已存在")
# else:
#     print(f"你输入的名字是{name},不存在")
