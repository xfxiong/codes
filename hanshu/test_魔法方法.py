# 定义init魔法方法设置初始化属性 并访问调用
'''
1.定义类
    init魔法方法：width height
    添加实例方法：访问实例属性
2.创建对象
3.调用实例方法
'''


class Washer():
    def __init__(self):
        self.width = 500
        self.height = 800

    def print_info(self):
        print('洗衣机的宽度是{}'.format(self.width))
        print('洗衣机的宽度是{}'.format(self.height))


haier = Washer()
haier.print_info()
