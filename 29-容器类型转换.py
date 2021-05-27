str1 = 'abcdegf'
list1 = [10, 20, 30, 40]
t1 = (10, 20, 30, 50)
s1 = {10, 20, 30, 40}
dict1 = {'name': 'Tom', 'age': 18}
# list()
print(list(str1))
print(list(t1))
print(list(s1))
print(list(dict1))

# tuple()
print(tuple(str1))
print(tuple(list1))
print(tuple(s1))
print(tuple(dict1))  # ('name', 'age')

# set()
print(set(list1))
print(set(t1))
print(set(str1))  # {'g', 'c', 'a', 'e', 'b', 'f', 'd'}
print(set(dict1))  # {'name', 'age'}
