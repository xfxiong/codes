# 需求：math 模块下sqrt() 平方根计算
'''
1.导入模块
2.测试是否导入成功：调用该模块内的 sqrt函数
'''
# 方法一：import 模块名；模块名.函数
# import math
# print(math.sqrt(9))

# #方法二：from 模块名 import 功能1，功能 2 ;功能调用（不需要书写模块名.功能）
# from math import sqrt
# print(sqrt(9))

# 方法三：from 模块名 import *  ；导入模块内所有功能，功能调用（不需要书写模块名.功能）
from math import *

print(sqrt(9))

# 需求：运行后暂停2秒打印hello
# 模块定义别名
import time as tt

tt.sleep(2)
# time.sleep(2)  报错
print('hello')

# 功能定义别名
from time import sleep as sl

sl(2)
print('hello lily')
