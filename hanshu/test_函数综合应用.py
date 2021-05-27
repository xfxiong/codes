'''
需求；
进入系统显示功能界面
功能如下：1.添加学员；2.删除学员；3.修改学员信息；4.查询学员信息
5.显示所有学员信息；6退出系统
步骤：
1.显示功能界面
2.用户输入功能序号
3.根据用户输入的功能序号，执行不同的功能（函数）
    定义函数
    调用函数

'''


# 显示功能选项界面
def print_info():
    print("请选择功能：——————------——")
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员信息")
    print("4.查询学员信息")
    print("5.显示所有学员信息")
    print("6.退出系统")
    print('-' * 20)


# 全局变量，所有学员信息存在列表中，每位学员的信息是字典数据
info = []


# 1.添加学员
def add_info():
    '''添加学员函数'''
    # 1.接收用户输入学员信息:学号、姓名，手机号，并保存
    new_id = input("请输入学号：")
    new_name = input("请输入姓名：")
    new_tel = input("请输入手机号码：")
    # 声明info为全局变量
    global info
    # 判断添加学员信息是否存在
    for i in info:
        # 已存在，报错提醒
        if new_name == i['name']:
            print('该用户已经存在！')
            # 退出当前函数，后面的代码不执行
            return
    # 用户不存在，准备空字典
    info_dict = {}
    # 输入的数据追加到字典，再列表追加字典数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # print(info_dict)
    # 列表追加字典
    info.append(info_dict)
    print(info)


# 2.删除学员
def del_info():
    '''删除学员'''
    # 1.输入要删除的学员姓名
    del_name = input("输入要删除的姓名：")
    global info
    # 判断学员是否存在，存在删除，否则报错
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    # 循环都执行完了，执行else
    else:
        print('该学员不存在')
    print(info)


# 3.修改学员信息
def modify_info():
    '''修改学员信息'''
    mod_name = input("请输入要修改的学员姓名：")
    global info
    for i in info:
        if mod_name == i['name']:
            i['tel'] = input("输入修改的手机号")
            break
    else:
        print('该学员不存在')
    print(info)


# 4.查询学员信息
def search_info():
    '''查询函数'''
    search_name = input("请输入查询的学员姓名：")
    global info
    for i in info:
        if search_name == i['name']:
            print('该学员的信息如下：')
            print('{0}的学号为{1}，手机号码为{2}'.format(i['name'], i['id'], i['tel']))
    else:
        print('该学员不存在')
    print(info)


# 5.显示所有
def print_all():
    '''显示所有学员信息'''
    print('学号\t姓名\t手机号')
    for i in info:
        print('{0}\t{1}\t{2}'.format(i['id'], i['name'], i['tel']))


# 系统功能需要循环使用，直到输入6退出
while True:
    # 1.显示功能界面
    print_info()
    # 2.用户输入功能序号
    user_num = int(input("请输入功能序号："))
    # 3.根据用户输入的功能序号，执行不同的功能（函数）
    if user_num == 1:
        # print("添加")
        add_info()
    elif user_num == 2:
        # print("删除")
        del_info()
    elif user_num == 3:
        # print("修改")
        modify_info()
    elif user_num == 4:
        # print("查询")
        search_info()
    elif user_num == 5:
        # print("显示所有")
        print_all()
    elif user_num == 6:
        # print("退出系统")
        # 要退出程序：  while true --break
        exit_flag = input("确定要退出吗？yes or no:")
        if exit_flag == 'yes':
            break
    else:
        print("输入的功能序号错误")
