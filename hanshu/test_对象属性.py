class Washer():
    def wash(self):
        print('能洗衣服')
        print(self)

    # 获取对象属性
    def print_info(self):
        # slef.属性值
        # print(self.width)
        print('洗衣机的宽度是{}'.format(self.width))
        print('洗衣机的宽度是{}'.format(self.height))


haier = Washer()

# 添加属性，对象名.属性名 = 值
haier.width = 500
haier.height = 800

# 类外面获取对象属性  对象名.属性名
# print('洗衣机的宽度是{}'.format(haier.width))
# print('洗衣机的高度是{}'.format(haier.height))

# 对象调用方法
haier.print_info()
