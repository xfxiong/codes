# 1.float()
num1 = 1
str1 = '10'
print(type(float(num1)))
print(float(num1))  # 1.0

print(float(str1))  # 10.0

# str()
print(type(str(num1)))
print(str(num1))

# tuple()
list1 = [1, 2, 3]
print(tuple(list1))

# list()
tt = (1, 3, 4)
print(list(tt))

# eval() 字符串中的数据转换为原本的类型
str2 = '1'
str3 = '1.1'
str4 = '(1,2,3)'
str5 = '[1,2,3]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
