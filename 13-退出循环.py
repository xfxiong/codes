# break ，退出循环；1.吃5个苹果，吃完第三个吃饱了，第4和第5不吃了
i = 1
while i <= 5:
    if i == 4:
        print("吃饱了，不吃了")
        break
    print(f'吃了第{i}个苹果')
    i += 1

# continue ，退出当前，继续执行下一次循环；
# 2.吃5个苹果，不吃第三个，开始吃第4个
i = 1
while i <= 5:
    if i == 3:
        print("有虫子，不吃了")
        # 使用continue之前一定要修改计数器
        i = i + 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
