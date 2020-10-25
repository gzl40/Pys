# -*- coding = utf-8 -*-
# @Time: 2020/4/9  23:27
# @Author: GZL
# @File: demon6.py
# @Software: PyCharm




# namelist = []     # 定义一个空列表

namelist = ["小张", "小王", "小李"]
'''
testlist = [1, "测试"]
print(type(testlist[0]))                  # 列表咳哟存储混合类型
print(type(testlist[1]))

print(namelist[0])
print(namelist[1])
print(namelist[2])

'''

'''
for name in namelist:
    print(name)

# print(len(namelist))                 # len（）可以得到列表的长度



length = len(namelist)

i = 0

while i < length:
    print(namelist[i])
    i += 1

'''


# 增加   ： [append]
'''
print("--------增加前·名单列表的数据--------")
for name in namelist:
    print(name)

nametemp = input("请输入姓名")
namelist.append(nametemp)         # 在末尾追加一个元素

print("--------增加后·名单列表的数据--------")
for name in namelist:
    print(name)
'''

'''
# 增   [entend]
a = [1,2]
b = [3,4]
a.append(b)             # 将列表当作一个元素加入
print(a)

a.extend(b)             # 将b列表中的每一个元素逐一追加到列表中
print(a)
'''

'''
# 增   [insert]

a = [0, 1, 2]
a.insert(1, 3)         # 第一个变量表示下标，第二个表示元素（对象）
print(a)               # 指定下标位置，插入元素
'''


'''
# 删   [del]     [pop]       [remove]

moviename = ["加勒比海盗", "骇客帝国", "第一滴血", "指环王", "速度与激情", "指环王"]

print("--------删除前·电影列表的数据--------")
for name in moviename:
    print(name)

# del moviename[2]                # 在指定位置删除一个元素
# moviename.pop()                   # 弹出末尾最后一个元素
moviename.remove("指环王")          # 直接删除指定元素

print("--------删除后·电影列表的数据--------")
for name in moviename:
    print(name)

'''


'''
# 改

print("--------增加前·名单列表的数据--------")
for name in namelist:
    print(name)

namelist[1] = "小红"       # 修改指定下标的元素内容

print("--------增加后·名单列表的数据--------")
for name in namelist:
    print(name)

'''


'''
# 查  ； 【in   ;    not in】

findname = input("请输入你要查找的学生姓名：")

if findname in namelist:
    print("在学员名单中找到了相同的名字")
else:
    print("没有找到")

'''


'''
mylist = ["a", "b", "c", "a", "b"]



print(mylist.index("a", 1, 4))            # 查找指定下标的元素，并返回找到对应数据的下标

print(mylist.index("a", 1, 3))            # 范围区间左闭右开, [  ,   )
                                          # 找不到会报错
                                    
print(mylist.count("a"))                 #统计某个元素出现几次

'''

'''
# 排序和反转
a = [1, 4, 2, 3]
print(a)
a.reverse()    # 将列表所有元素反转
print(a)

a.sort()
print(a)       # 升序

a.sort(reverse=True)      # 降序
print(a)
'''

'''
# schoolNames = [[], [], []]       # 有三个元素的空列表，每个元素都是一个空列表

schoolNames = [["北京大学", "清华大学"], ["南开大学", "天津大学", "天津师范大学"], ["山东大学", "中国海洋大学"]]

print(schoolNames[0][0])
'''

import random

offices = [[], [], []]

names = ["A", "B", "C", "D", "E", "F", "G", "H"]

for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d的人数为%d"%(i, len(office)))
    i += 1
    for name in office:
        print("%s"%name, end="\t")
    print("\n")
    print("-"*20)





