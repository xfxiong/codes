# 二次方程式 ax**2 + bx + c = 0 ，x=
# a、b、c 用户提供，为实数，a ≠ 0

# 导入 cmath(复杂数学运算) 模块
import cmath

a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))

d = b ** 2 - 4 * a * c

# 两个解
so1 = (-b + cmath.sqrt(d)) / (2 * a)
so2 = (-b - cmath.sqrt(d)) / (2 * a)

print("二次方程的解是{0}，{1}".format(so1, so2))
