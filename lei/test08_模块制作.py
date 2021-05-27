# 1.导入模块
import my_module1

# 2.调用功能
my_module1.testA(1, 3)

print(my_module1)

# 拓展：名字重复
# 问题：import 模块名  功能名字重复没有影响
import time

print(time)

time = 1
print(time)  # 1
# 为什么变量能覆盖模块，python语言中，数据通过引用传递的
