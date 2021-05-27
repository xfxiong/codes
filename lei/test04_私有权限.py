class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print('运用{}制作煎饼果子'.format(self.kongfu))


class School(object):
    def __init__(self):
        self.kongfu = '[培训煎饼果子配方]'

    def make_cake(self):
        print('运用{}制作煎饼果子'.format(self.kongfu))


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'
        # self.money =2000000  #公有属性
        self.__money = 2000000  # 私有属性

    # 定义函数：获取私有属性值 get_XX
    def get_money(self):
        return self.__money

    # 定义函数：修改私有属性值 set_XX
    def set_money(self):
        self.__money = 500

    # 定义私有方法
    def __info_print(self):
        print('这是私有方法')

    def make_cake(self):
        self.__init__()
        print('运用{}制作煎饼果子'.format(self.kongfu))

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(Prentice):
    pass


daqiu = Prentice()

xiaoqiu = Tusun()

print(xiaoqiu.get_money())
xiaoqiu.set_money()
print(xiaoqiu.get_money())
