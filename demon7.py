# -*- coding = utf-8 -*-
# @Time: 2020/4/13  21:50
# @Author: GZL
# @File: demon7.py
# @Software: PyCharm



'''
tup1 = ()   # 创建空的元组
print(type(tup1))


# tup2 = (50)    #class int
# tup2 = (50,)
tup2 = (50, 60, 70)
print(type(tup2))   # <class 'tuple'>

'''

'''
tup1 = ("abc", "def", 2000, 2020, 333, 444, 555, 666)

print(tup1[0])
print(tup1[-1])          # 访问最后一个元素
print(tup1[1:5])         # 左闭右开
'''



'''
# 增       (连接）

tup1 = (12, 34, 56)
tup2 = ("abc", "xyz")
tup = tup1 + tup2
print(tup)
'''

'''
# 删
tup1 = (12, 34, 56)
print(tup1)
del tup1       # 删除了整个元组变量
print("删除后")
print(tup1)

'''


'''
# 改
tup1 = (12, 34, 56)

tup1[0] = 100         # 报错，不允许修改
'''


# 字典的定义
info = {"name": "吴彦祖", "age": 18}
# 字典的访问
'''
print(info["name"])
print(info["age"])
'''

# 访问了不存在的键
# print(info["gender"])       # 直接访问会报错

# print(info.get("gender"))     # 使用get方法，没有找到对应的键，默认返回：None


'''
print(info.get("age", 20))
print(info.get("gender", "m"))   # 没找到，可以设定默认值
'''

# 增
'''
info = {"name": "吴彦祖", "age": 18}
newID = input("请输入学号")
info["id"] = newID

print(info["id"])
'''

# 删

# del
'''
info = {"name": "吴彦祖", "age": 18}
print("删除前：%s" % info["name"])

del info["name"]
'''

# print("删除后：%s" % info["name"])   #删除指定键值对后，再次访问会报错
'''
info = {"name": "吴彦祖", "age": 18}
print("删除前%s" % info)

del info
'''
# print(info)                  #删除字典后，再访问报错


# clear    清空

'''
info = {"name": "吴彦祖", "age": 18}
print("清除前%s" % info)

info.clear()

print("清除后%s" % info)
'''




# 改
'''
info = {"name": "吴彦祖", "age": 18}

info["age"] = 20

print(info["age"])

'''


# 查        （遍历）

info = {"id":1, "name": "吴彦祖", "age": 18}
'''
print(info.keys())          # 得到所有的键，列表的形式

print(info.values())        # 得到所有的值，列表的形式

print(info.items())         # 得到所有的项 ， 每个键值对是一个元组
'''
'''
# 遍历所有的键
for key in info.keys():
    print(key)
'''
'''
# 遍历所有的值
for value in info.values():
    print(value)
'''
'''
# 遍历所有的键值对
for key, value in info.items():
    print("key=%s, value=%s" % (key, value))
'''

# 使用枚举函数同时拿到列表中的下标和元素内容
mylist = ["a", "b", "c", "d"]

for i, x in enumerate(mylist):
    print(i, x)




