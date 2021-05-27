# 用户年龄大于等于18，成年可以上网
age = int(input("请输入你的年龄:"))
if age >= 18:
    print(f"你的年龄是{age},已经成年，可以上网")
else:
    print(f"你的年龄是{age},未成年，不能上网")

'''
年龄小于18是童工
18-60 合法
大于60 退休
'''
age = int(input("请输入你的年龄："))

if age < 18:
    print(f"你输入的年龄是{age},童工")
# elif (age>=18) and (age <=60):
elif 18 <= age <= 60:
    print("你输入的年龄是{}".format(age), "，合法")
else:
    print("你输入的年龄是{}".format(age), "，退休年龄")
