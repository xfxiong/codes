def userinfo(name, age, gender):
    print('你的名字是{},年龄是{}，性别是{}'.format(name, age, gender))


# 位置参数
userinfo('TOM', 20, '男')  # 传递和定义的参数 顺序，个数一致

# 关键字参数  键=值
userinfo('Rose', gender='女', age=20)
# 位置参数必须在关键字参数前，关键字参数不分顺序
userinfo(gender='女', name='rose', age=20)


# 缺省参数，定义函数时给参数提供默认值，位置参数在默认参数前，传参则修改默认值
def user_info(name, age, gender='男'):
    print('你的名字是{},年龄是{}，性别是{}'.format(name, age, gender))


user_info('Lily', 18)  # 默认值
user_info('Rose', 20, '女')  # 修改了缺省参数 修改了默认值


# 不定长参数
# 包裹位置传递,args是元组类型
def userinfos(*args):
    print(args)


userinfos('TOM')  # ('TOM',)
userinfos('TOM', 18)  # ('TOM', 18)


# 包裹关键字传递
def userInfo(**kwargs):
    print(kwargs)


userInfo()  # {}
userInfo(name='TOM', age=20, id=110)
# {'name': 'TOM', 'age': 20, 'id': 110}
