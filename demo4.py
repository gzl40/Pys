# -*- coding = utf-8 -*-
# @Time: 2020/4/7  23:08
# @Author: GZL
# @File: demo4.py
# @Software: PyCharm
'''
for i in range(5):
    print(i)
'''

'''
for i in range(0, 10, 3):
    print(i)
'''

'''
for i in range(-10, -100, -30):
    print(i)
'''

'''
name = "guangzhou"

for x in name:
    print(x, end="\t")
'''

'''
a = ["aa", "bb", "cc", "dd"]
print(len(a))
for i in range(len(a)):
    print(i, a[i])
'''

'''
i = 0
while i < 5:
    print("当前是第%d次执行循环" % (i+1))
    print("i=%d" % i)
    i += 1
'''

'''
# 1-100 求和
i = 0
a = 0
while i < 101:
    print("当前i等于%d" % i, end="\t")
    a += i
    print("当前和为%d" % a, end="\n")
    i += 1
'''

'''
# 1-100 求和
n = 100
su = 0
counter = 1
while counter <= n:
    su = su + counter
    counter += 1

print("1到%d的和为%d" % (n, su))

'''

'''
# while-else
count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "大于或等于5")
'''

'''
i = 0
while i < 10:
    i = i +1
    print("-"*30)
    if i == 5:
        break          # 结束整个循环
    print(i)
'''

i = 0
while i < 10:
    i = i +1
    print("-"*30)
    if i == 5:
        continue       # 结束本次循环
    print(i)
