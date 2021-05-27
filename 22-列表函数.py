my_list = ['lily', 'Tom', 'Rose']

# del
# del my_list
# del(my_list)

# 删除指定下标数据
del my_list[0]
print(my_list)

# pop() 删除指定下表数据，不指定的话，删除最后一个，pop函数会返回被删除的数据
del_name = my_list.pop()
# del_name =my_list.pop(1)
print(del_name)
print(my_list)

name_list = ['Tom', 'Wendy', 'Lily', 'Andy', 'Lily']

# 修改指定下标的数据
name_list[2] = 'David'
print(name_list)

# 逆序
list1 = [1, 2, 3, 4, 5]
list1.reverse()
print(list1)

# sort() 排序 升序降序
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

# remove() 移除某一个匹配的数据
name_list.remove('Lily')
print(name_list)

# clear()  清空列表
name_list.clear()
print(name_list)

list2 = list1.copy()
print(list2)
