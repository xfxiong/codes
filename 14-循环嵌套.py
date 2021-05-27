# 打印三角形
# 一行输出的星星和行号是相等的
print("打印三角形——————")
j = 0
while j < 5:
    i = 0
    while i <= j:
        print("*", end="")
        i += 1
    print()
    j += 1

print("打印正方形————————")
# 打印星号（正方形）
b = 0
while b < 5:
    a = 0
    while a < 5:
        print("*", end='')
        a += 1
    # 一行星星结束，换行显示下一行
    print()
    b += 1

# 循环嵌套
i = 0
while i < 3:
    j = 0
    while j < 3:
        print("我错了")
        j += 1
    print("刷碗")
    print("今天惩罚结束——————")
    i += 1
print("惩罚结束——————")
