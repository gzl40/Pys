# -*- coding = utf-8 -*-
# @Time: 2020/4/8  7:58
# @Author: GZL
# @File: 九九乘法表.py
# @Software: PyCharm


a = 1
b = 1
for a in range(1, 10):
    for b in range(1, 10):
        if b > a:
            print(end="\n")
            break
        print("%d X %d = %d"%(a, b, a * b), end="\t")
