# filter()
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 过滤序列中的偶数，留下符合条件的
def func2(x):
    return x % 2 == 0


# 调用filter
result = filter(func2, list2)
print(list(result))

# reduce()  1.导入模块
import functools

list1 = [1, 2, 3, 4, 5]


# 2.定义功能函数
def func1(a, b):
    return a + b


# 3.调动reduce：作用：功能函数计算结果继续和序列的下一个元素做累积计算
result = functools.reduce(func1, list1)
print(result)

# map()   1.准备列表数据
list1 = [1, 2, 3, 4, 5]


# 2.准备2次方计算的函数
def func(x):
    return x ** 2


# 3.调用map
result = map(func, list1)

# 4.验收成果
print(result)  # 返回一个迭代器，内存地址 <map object at 0x000001D81EB48160>
print(list(result))
