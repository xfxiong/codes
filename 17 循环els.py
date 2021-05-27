'''
1.书写循环
2.循环正常结束执行的代码
'''
# while..else   break
i = 1
while i < 5:
    if i == 3:
        print("说的不真诚")
        break
    print("我错了")
    i += 1
else:
    print("原谅了")

print("while..else;  continue————————————")
i = 1
while i < 5:
    if i == 3:
        print("说的不真诚")
        i += 1
        continue
    print("我错了")
    i += 1
else:
    print("原谅了")
