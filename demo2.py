# -*- coding = utf-8 -*-
# @Time: 2020/4/5  23:12
# @Author: GZL
# @File: demo2.py
# @Software: PyCharm

'''
print("标准化输出字符串")

a = 10

print("这是变量:" , a)

'''

# 格式化输出

age = 16
print("我的名字是%s,我的国籍是%s" % ("小哲", "中国"))
print("我的年纪是：%d" % age)

print("aaa", "bbb", "ccc")
print("www", "baidu", "com", sep=".")
print("hello", end="")
print("world", end="\t")
print("python", end="\n")
print("end")

'''


print("1234567890----------")
print("1234567890\n--------")

password = input("请输入密码")
print("您刚刚输入的密码是", password)



a = input("输入")
print(type(a))        # 输出字符串类型

print("输入一个数字%s" % a)

'''

a = int("123")
print(type(a))
b = a + 100
print(b)


c = int(input("输入"))          # 强制类型转化
print(type(c))        # 输出字符串类型

print("输入一个数字%d" % c)


