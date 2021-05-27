# 继承，子类默认继承父类的所有属性和方法
# 父类A
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


# 子类B
class B(A):
    pass


# 创建对象，验证结论
result = B()
result.info_print()  # 1
