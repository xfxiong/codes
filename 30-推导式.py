# [(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
list1 = []
for i in range(1, 3):
    for j in range(3):
        list1.append((i, j))
print(list1)

# 多个for实现列表推导式,等于for循环嵌套
list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2)

# 列表推导式  需求：创建一个0-10的列表,创建、控制有规律的列表

# while
list1 = []
i = 0
while i < 11:
    list1.append(i)
    i += 1
print(list1)

# for
list1 = []
for i in range(11):
    list1.append(i)
print(list1)

# 列表推导式
list1 = [i for i in range(11)]
print(list1)

# 需求：创建0-10的偶数列表
list2 = [i for i in range(0, 10, 2)]
print(list2)

list2 = []

for i in range(10):
    if i % 2 == 0:
        list2.append(i)
print(list2)

# 带if的列表推导式
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)
