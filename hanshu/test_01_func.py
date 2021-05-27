help(len)  # 查看函数的说明文档（函数的解释说明信息）


# 计算器,计算两数之和，并保存结果
def caculator(a, b):
    '''计算两数之和'''
    return a + b


a = int(input("输入a:"))
b = int(input("输入b:"))
c = caculator(a, b)
print("a+b的结果是:", c)

help(caculator)


# 返回值
def buy():
    return '烟'


goods = buy()
print(goods)


# 一个函数完成两个数1和2的加法运算，如何书写程序？
def num_add(a, b):
    '''
    求和函数
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    '''
    result = a + b
    print(result)


num_add(1, 2)


# 2.确定 选择功能界面
def sel_func():
    print("显示余额")
    print('存款')
    print('取款')


# 搭建整理框架
print("登录成功")
# 显示选择功能
sel_func()
print("显示余额")
sel_func()
print("取1000元钱")
sel_func()
