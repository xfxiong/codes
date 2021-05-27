# 一个函数多个返回值
def return_num():
    # return 1,2
    # return (1,2)
    # return [100,200]
    return {'name': 'lily', 'age': 20}


result = return_num()
print(result)  # (1,2) 默认返回元组

# return 元组、列表、字典；返回多个值
