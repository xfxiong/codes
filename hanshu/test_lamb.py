print('lambda匿名函数的应用-------------')
# 带判断的lambda
fn = lambda a, b: a if a > b else b
print(fn(1000, 500))

# 列表数据按字典key值排序
students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 22},
    {'name': 'Lily', 'age': 19}
]

# 排序 sort(key=lambda ...,reverse=bool数据）
# 1.name key 对应的值进行升序排序
students.sort(key=lambda x: x['name'])
print(students)

# 2.name key 对应的值进行降序排序
students.sort(key=lambda x: x['name'], reverse=True)
print(students)

# 3.age key 对应的值进行升序排序
students.sort(key=lambda x: x['age'])
print(students)

print('lambda匿名函数的参数形式-------------')
# 1.无参数
fn1 = lambda: 100
print(fn1())

# 2.一个参数
fn2 = lambda a: a
print(fn2(2))

# 3.默认参数（缺省参数，可以传值或不传）
fn3 = lambda a, b, c=100: a + b + c
print(fn3(1, 2))
print(fn3(1, 2, 200))

# 4.可变参数：*args ，返回值为元组
fn4 = lambda *args: args
print(fn4(1, 2))
print(fn4(1, 2, 20, 50, 40))
print(fn4(10))

# 5.可变参数：**kwargs ,返回值为字典
fn5 = lambda **kwargs: kwargs
print(fn5(name='python', age=18))
print(fn5(age=18))

print("lambda匿名函数体验------------")


# 函数:返回值200
def fn1():
    return 200


print(fn1())

# 匿名函数--lambda （参数列表）:表达式
# 只有一个返回值
fn2 = lambda: 100
print(fn2)  # lambda内存地址

# 100 返回值，调用函数
print(fn2())


# 函数计算a+b
def add(a, b):
    return a + b


print(add(1, 2))

# lambda 实现a+b
fn3 = lambda a, b: a + b
print(fn3(1, 2))
