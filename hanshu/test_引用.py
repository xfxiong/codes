# int类型
a = 1
b = a
print(b)  # 1

# a 和 b的id值一样
print(id(a))  # id()  检测两个变量的id值--内存的十进制值
print(id(b))

a = 2
print(b)  # 1 ，int 类型是不可变类型

print(id(a))  # 修改了a,内存要开辟另外一份内存地址
print(id(b))

# 列表
aa = [10, 20]
bb = aa
print(bb)

print(id(aa))  # 1816966337856
print(id(bb))  # 1816966337856

aa.append(30)
print(aa)
print(bb)  # 列表是可变类型

print(id(aa))  # 1816966337856
print(id(bb))  # 1816966337856


# 引用当实参
# 定义函数-形参；访问打印形参看是否有数据；访问形参id,改变形参数据，查看形参打印id
# 调用函数 --把可变和不可变类型依次当实参传入
def test1(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))


b = 100
test1(b)

c = [11, 22]
test1(c)

# 可变类型 --- 列表、集合、字典 ,可以直接修改
# 不可变类型 -- 元组、整型、浮点数、字符串，不能直接修改
