# 任意两个数字，先进性数字处理后（绝对值或四舍五入）再求和计算
# 方法一
def add_num(a, b):
    return abs(a) + abs(b)


print(add_num(-1, 2))


# 写法二：高阶函数 f是第三个参数，用来接收传入的函数
def sum_num(a, b, f):
    return f(a) + f(b)


print(sum_num(-1, -2, abs))
print(sum_num(1.2, 1.9, round))

# abs()   对数字求绝对值计算
print(abs(-10))
# round() 对数字的四舍五入计算
print(round(1.9))
print(round(1.2))
