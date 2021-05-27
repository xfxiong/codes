# 共用全局变量
# 1.声明一个全局变量2.定义两个函数3.函数一修改全局变量，函数2访问全局变量
glo_num = 0


def test1():
    global glo_num
    glo_num = 100


def test2():
    print(glo_num)


print(glo_num)  # 0 ,修改的函数没有执行
test1()
test2()
print(glo_num)  # 100，调用了函数1
