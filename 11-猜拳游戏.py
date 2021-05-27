'''
参与的有：
玩家：手动出拳
电脑：随机出拳
判断输赢
玩家胜，电脑胜，平局

'''
import random

player = int(input("请出拳：（0--石头；1--剪刀；2--布）"))
# random.randint(开始数字，结束数字）
computer = random.randint(0, 2)
print("电脑出拳：", computer)
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print("玩家获胜")
elif player == computer:
    print("平局，再来一局")
else:
    print("电脑获胜")
