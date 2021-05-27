# 求三个数之和
def sum_num(a, b, c):
    return a + b + c


result = sum_num(1, 2, 3)
print(result)


# 三个数平均数
def average_num(a, b, c):
    # result1 =a+b+c
    result1 = sum_num(a, b, c)
    return result1 / 3


average_result = average_num(1, 2, 3)
print(average_result)


# 打印一条横线
def print_line():
    print('-' * 20)


# 打印多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(5)
