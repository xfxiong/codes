class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print('运用{}制作煎饼果子'.format(self.kongfu))


class School(Master):
    def __init__(self):
        self.kongfu = '[培训煎饼果子配方]'

    def make_cake(self):
        print('运用{}制作煎饼果子'.format(self.kongfu))

        # 2.1 super()带参数写法
        # super(School,self).__init__()
        # super(School, self).make_cake()
        # 2.2 无参数的super
        super().__init__()
        super().make_cake()


class Prentice(School):
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

    # 需求：一次性调用父类School Master的方法
    def make_old_cake(self):
        # 方法一：如果定义的类名修改，这里也要修改，代码量大，冗余
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

        # 方法二：super()

        # 方法2.1 super(当前类名，self).函数()
        # super(Prentice, self).__init__()
        # super(Prentice,self).make_cake()

        # 2.2 super().函数()
        super().__init__()
        super().make_cake()


daqiu = Prentice()
daqiu.make_old_cake()
