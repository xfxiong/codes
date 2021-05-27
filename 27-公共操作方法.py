# in \not in
print('a' in 'abcd')
print('a' not in 'abcd')

list11 = ['a', 'b', 'c', 'd']
print('a' in list11)

t1 = ('a', 'b', 'c')
print('a' in t1)

dict1 = {'name': 'Tom', 'age': 20}
print('name' in dict1)
print('name' in dict1.keys())
print('name' not in dict1.values())

str1 = 'a'
list1 = ['hello']
t1 = ('world',)
# * ：复制，不支持字典
print(str1 * 5)

# 打印10个-
print('-' * 10)

print(list1 * 5)
print(t1 * 5)

str1 = 'hello'
str2 = 'lily'

list1 = [1, 2]
list2 = [10, 20]

t1 = (1, 2)
t2 = (10, 20)

dict1 = {'name': 'Tom'}
dict2 = {'age': 20}

# +:合并  不支持字典
print(str1 + str2)
print(list1 + list2)
print(t1 + t2)
