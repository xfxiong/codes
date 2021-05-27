# 集合推导式
# 创建一个集合，数据为下方列表的2次方
list1 = [1, 1, 2]
set1 = {i ** 2 for i in list1}
print(set1)
# 集合有自动去重功能


# 1.创建一个字典，key是1-5，value是数字的2次方
dict1 = {i: i ** 2 for i in range(1, 5)}
print(dict1)

# 将两个列表合并为一个字典
list1 = ['name', 'age', 'gender']
list2 = ['Lily', 20, 'female']
dict2 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict2)

# 如果两个列表数据相同，任意列表长度都可以；如果长度不同，使用数据少的列表长度

# ****提取字典中目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 200}
# 提取数量大于200的数据
# print(counts.items())
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)
