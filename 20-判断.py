mystr = "hello world and itcast and itima and python"
# startswith()
# print(mystr.startswith('hello'))
# print(mystr.startswith('hel'))
# print(mystr.startswith('hels'))

# #endswith()
# print(mystr.endswith('python'))
# print(mystr.endswith('pythons'))

# isalpha() 检查字符串是否都是字母
print(mystr.isalpha())
# isdigit() 检查字符串是否都是数字
print(mystr.isdigit())
mystr2 = '123456'
print(mystr2.isdigit())
# isalnum() 检查字符串中数字或字母或组合
print(mystr.isalnum())
mystr1 = 'abc123'
print(mystr1.isalnum())
# isspace() 字符串中只包含空白
print(mystr.isspace())
mystr3 = '  '
print(mystr3.isspace())
