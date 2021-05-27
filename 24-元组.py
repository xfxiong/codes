tt = ('aa', 'bb', 'cc', 'dd')

t1 = ('aa', 'bb', ['cc', 'dd'])

print(t1[2])
print(t1[2][0])
t1[2][0] = 'Tom'
print(t1)

# t1 =(10,20,30)
# print(t1)
# t2 =(10,)
# print(type(t2))


# 下标
print(tt[0])

# index()  返回开始下标
print(tt.index('bb'))

# count()
print(tt.count('bb'))

# len()
print(len(tt))
