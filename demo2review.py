# -*- coding = utf-8 -*-
# @Time: 2020/4/6  9:16
# @Author: GZL
# @File: demo2review.py
# @Software: PyCharm
print("标准化输出字符串")
a = 10
print(a)              # 输出变量

'''
占位符
'''
year = 2020
print("今年是%d年" % year)        # 数字占位符
print("2019nCoV origin in %s , spread to %s" % ("武汉", "世界"))       # 字符占位符

print("aaa", "bbb", "ccc")
print("www", "gdfz", "cn", sep=".")

print("hello", end="")
print("world", end="\t")
print("python", end="\n")
print("return 0")
