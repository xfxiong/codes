# 家具类
class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 房屋类
class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return '房子的地理位置是{}，房屋面积是{}，房屋剩余面积是{}，家具有{}'.format(self.address, self.area, self.free_area, self.furniture)

    def add_furniture(self, item):
        '''添加家具'''
        # 如果家具占地面积小于房子剩余明基，可以搬入--家具列表添加家具名字数据并更新房子剩余面积
        # 家具面积太大，无法容纳
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            self.free_area -= item.area

        else:
            print('家具面积太大，无法容纳')


# 双人床，6
bed = Furniture('双人床', 6)

jia1 = Home('beijing', 60)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

ball = Furniture('篮球场', 2000)
jia1.add_furniture(ball)  # 家具面积太大，无法容纳
print(jia1)
