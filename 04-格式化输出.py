# str.format()格式化输出
print('站点列表 {0:6}, {1:7},{2:5d}和{other:.2f}'.format('Google', 'Runoob', 1815, other=3.14159))

'''
准备数据
格式化输出数据
'''
# 1.今年我的年龄是X岁
age = 18
print('今年我的年龄是%d' % age)
# 2.我的名字是X
name = 'TOM'
print('我的名字是%s' % name)
# 3.我的体重是X
weight = 56.5
print('我的体重是%f' % weight)
print('我的体重是%.2f' % weight)
# 4.我的学号是X
stu_id = 1
print('我的学号是%d' % stu_id)

# 学号是001
print('我的学号是%03d' % stu_id)

# 5.我的名字是X，今年X岁了
print("我的名字是%s，今年%d岁了" % (name, age))

# 明年X岁
print("我的名字是%s，明年%d岁了" % (name, age + 1))

# 6.我的名字是X，今年X岁了，体重X公斤，学号是X
print("我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%03d" % (name, age, weight, stu_id))

print("我的名字是%s，今年%s岁了，体重%s公斤" % (name, age, weight))
# f格式化字符串 python3.6以后的版本
print(f'我的名字是{name}，今年{age}岁了，体重{weight}公斤')
