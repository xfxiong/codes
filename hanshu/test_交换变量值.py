# 交换变量
# 方法一 第三变量存储
a = 10
b = 20

# 定义第三变量
c = 0
# a的数据存到c
c = a
# b的数据赋值给a
a = b
# c的数据赋值到b
b = c
print(a)
print(b)

# 方法二
a, b = 1, 2
a, b = b, a
print(a)  # 2
print(b)  # 1
