ss = {10, 20, 30, 40, 50}
# in 或 not in 判断数据是否存在
print(10 in ss)  # True
print(10 not in ss)  # False

# pop() ，随机删除一个数据，并返回数据
del_num = ss.pop()
print(del_num)
print(ss)

# remove() ，不存在报错
ss.remove(10)
print(ss)
# ss.remove(10)
# print(ss)

# discard() ，不存在不报错
ss.discard(20)
print(ss)
ss.discard(20)
print(ss)

s4 = {10, 20}
# update()
s4.update([10, 20, 30, 40, 50])
print(s4)  # {40, 10, 50, 20, 30}
# add
s4.add(100)
print(s4)

# 创建有数据的集合
s1 = {10, 20, 30, 40, 50, 40, 50}
print(s1)
# {40, 10, 50, 20, 30}
# 打印的数据没有顺序，不能有重复数据，重复数据自动去重

s2 = set('abcdefg')
print(s2)
# {'d', 'e', 'g', 'c', 'b', 'f', 'a'}
# 空集合
s3 = set()
print(s3)
