# 1.定义类：初始化属性、被烤、和添加调料的方法，显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        '''烤地瓜方法'''
        # 1.计算地瓜整体考过的时间
        self.cook_time += time
        # 2.用整体考过的时间判断地瓜的状态
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state = '烤糊了'

    def add_condiments(self, condiment):
        '''添加调料'''
        # 把用户需要的调料追加到列表
        self.condiments.append(condiment)

    def __str__(self):
        return '这个地瓜烤了{0}分钟，状态是{1}，调料有{2}'.format(self.cook_time, self.cook_state, self.condiments)


# 2. 创建对象并调用对应的实例方法
digua1 = SweetPotato()
print(digua1)

digua1.cook(2)
digua1.add_condiments('辣椒面')
print(digua1)

digua1.cook(2)  # 2+2=4分钟
digua1.add_condiments('酱油')
print(digua1)
