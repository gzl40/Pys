# -*- coding = utf-8 -*-
# @Time: 2020/4/7  22:39
# @Author: GZL
# @File: 石头剪刀布.py
# @Software: PyCharm

'''
import random
a = int(input("石头2，剪刀1，布0"))
b = random.randint(0, 2)
print("对方编号%d" %b)
if b == 0:
    print("对方出布")
    if a == 1:
        print("you win")
    if a == 2:
        print("you lose")
    if a == 0:
        print("平")
if b == 1:
    print("对方出剪刀")
    if a == 2:
        print("you win")
    if a == 0:
        print("you lose")
    if a == 1:
        print("平")
if b == 2:
    print("对方出石头")
    if a == 0:
        print("you win")
    if a == 1:
        print("you lose")
    if a == 2:
        print("平")
'''

import random
a = int(input("石头2，剪刀1，布0"))
b = random.randint(0, 2)
print("对方编号%d" %b)
if a == b + 1 and a != 0:
    print("you win")
if a != b + 1 and a != 0:
    if a == b:
        print("平")
    else:
        print("you lose")
if a == 0:
    if b == 2:
        print("you win")
    if b == 1:
        print("you lose")
if a == b:
    print("平")




