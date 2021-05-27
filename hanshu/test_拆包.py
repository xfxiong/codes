# 拆包 元组
def return_num():
    return 100, 200


num1, num2 = return_num()
print(num1)
print(num2)

# 拆包 字典
dict1 = {'name': 'lily', 'age': 20}
# 两个键值对，用两个变量
a, b = dict1
# key的值
print(a)  # name
print(b)  # age

# valu 值
print(dict1[a])  # lily
print(dict1[b])  # 20
