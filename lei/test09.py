# 方法一：import 包名.模块名    包名.模块名.功能()
# import lei.my_module1
# lei.my_module1.info_print1()

# 方法二，__init__.py中的all列表，添加允许导入的函数
# from 包名 import *  模块名.功能

from lei import *

my_module1.info_print1()
