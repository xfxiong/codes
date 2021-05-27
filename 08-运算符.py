# 复合赋值运算符
a = 10
a += 1  # a = a+1
print(a)

b = 10
b -= 1
print(b)

c = 10
c += 1 + 2
print(c)

d = 10
d *= 1 + 4
print(d)
# 先算右侧运算1+4，再算赋值运算符*


print((a < b) and (b < c))
print(a < b and b < c)
print((a > b) or (b < c))
print(not a)
print(not (a > b))
