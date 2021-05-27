'''
while 条件:
	条件成立重复执行的代码
	......

打印5遍我错了
'''
i = 0
while i < 5:
    print("我错了")
    i += 1

# 1-100的累加,5050,验证结果--改小数字
number = 0
i = 0
while i < 101:
    number += i
    i += 1
print(number)

# 1-100偶数的累加,2550
number = 0
i = 0
while i < 101:
    number += i
    i += 2
print(number)

# 第二种偶数累加方法
number = 0
i = 0
while i < 101:
    if i % 2 == 0:
        number += i
    i += 1
print(number)

# 第三种偶数累加方法
number = 0
i = 0
while i < 101 and i % 2 == 0:
    number = +i
    i += 1
print(number)
