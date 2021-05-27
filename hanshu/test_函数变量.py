# 定义一个函数，再声明一个变量
def testa():
    s = 10
    print(s)


testa()
# print(s)  报错，函数内部的局部变量不能使用

# 全局变量
a = 100


def testA():
    print(a)


def testB():
    # a=200   #这个a是局部变量
    # print(a)
    # 声明a为全局变量
    global a
    a = 200
    print(a)


testA()
testB()
print(a)

'''
如果函数里面直接把变量a=200，此时的a全局变量
先声明全局变量global a，再进行赋值，此时全局变量a被修改
'''
