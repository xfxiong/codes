'''
for 临时变量 in 序列：
    代码

1.准备一个序列
2.for循环
'''
# for..else 和while ...else


# for...break,不打印e
str1 = 'itehema'
for i in str1:
    if i == 'e':
        break
    print(i)

# for...continue，不打印e
str2 = 'ithema'
for i in str2:
    if i == 'e':
        continue
    print(i)
