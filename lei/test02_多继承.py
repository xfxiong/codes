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

    def make_cake(self):
        self.__init__()
        print('运用{}制作煎饼果子'.format(self.kongfu))

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 徒孙类1.创建类，用这个类创建对象；2.用这个对象调用父类的属性和方法
class Tusun(Prentice):
    pass


xiaoqiu = Tusun()
xiaoqiu.make_school_cake()
xiaoqiu.make_cake()
xiaoqiu.make_master_cake()
