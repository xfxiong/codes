# 需求：有三个办公室，8位老师，8位老师随机分配到3个办公室
'''
1.准备数据
    8位老师——列表
    3个办公室--列表嵌套
2.分配老师到办公室
    随机--办公室列表中追加老师名字
3.验证是否分配成功
    打印每个办公室人数和对应名字
'''
import random

# 准备数据
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]
# 分配老师到办公室--取到每个老师，放到办公室
for teacher in teachers:
    # 列表追加数据--append()
    # 不能指定下标，要用随机数
    num = random.randint(0, 2)
    offices[num].append(teacher)

print(offices)
# 给每个办公室添加编号
i = 1
# 验证是否分配成功
for office in offices:
    print(f"办公室{i}的人数是：{len(office)},老师分别是：")
    # 打印老师的名字
    for name in office:
        print(name)
    i += 1
