str1 = 'abcdegf'
list1 = [10, 20, 30, 40]
t1 = (10, 20, 30, 50)
s1 = {10, 20, 30, 40}
dict1 = {'name': 'Tom', 'age': 18}

# len() 元素个数
print(len(str1))
print(len(list1))
print(len(t1))
print(len(s1))
print(len(dict1))

# del 目标 del(目标)
del (list1[0])
print(list1)
del dict1['name']
print(dict1)

# max() 元素最大值
print(max(str1))
print(max(list1))
print(max(t1))

# min()  元素最小值
print(min(str1))
print(min(list1))

# range(start,end,step)  供for循环使用，不包含最后一位数
print('-----')
for i in range(1, 10, 1):
    print(i, end=' ')

for i in range(1, 10, 2):
    print(i, end=' ')
# 没有开始就从0开始，没有步长就是默认1
for i in range(10):
    print(i, end=' ')
print('\n')
print("enumerate()函数-------")
# enumerate(可遍历对象，start=0)  start设置遍历数据的下标起始值默认0

list2 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list2):
    print(i)

for i in enumerate(list2, start=1):
    print(i)
