# 打开
f = open('txt.txt', 'w')
# 操作
f.write('aaa')
# 关闭
f.close()

'''
访问模式对文件的影响
访问模式对write()的影响
访问模式是否可用省略
'''
# r:如果文件不存在，报错；不支持写入操作，表示只读
# f = open('text1.txt','r')
f = open('txt.txt', 'r')
# f.write('aaa')
f.close()

# w:只写，如果文件不存在，新建文件；执行写入，会覆盖原有内容
f = open('1.txt', 'w')
f.write('aaa')
f.close()

# a:追加
f = open('1.txt', 'a')
f.write('bbb')
f.close()

# 访问模式参数可以省略，如果省略，表示访问模式为r
