# -*- coding = utf-8 -*-
# @Time: 2020/4/11  23:19
# @Author: GZL
# @File: 商品与购物车.py
# @Software: PyCharm



products = [["iphone",6888], ["MacPro",14800], ["小米6",2499], ["Coffee",31], ["Book",60], ["Nike",699]]

print("--------商品列表--------")

i = 0
for product in products:
    print(i, end="\t\t")
    print(products[i][0], end="\t\t")
    print(products[i][1])
    i += 1

shopping_list = []


while 1:
    request = input("如需退出请按 q  , Enter 以继续  ")
    print(end="\n\n\n")
    if request =="q":
        break
    a = int(input("输入商品序号"))
    print("您选择了%s,价格%d" % (products[a][0], products[a][1]))

    shopping_list.append(products[a])

num = 0

print("--------购物车--------")
for items in shopping_list:
    print(num + 1, end="\t")
    print(shopping_list[num][0], end="\t")
    print(shopping_list[num][1])
    num += 1

count = 0
bill = 0

for payment in shopping_list:
    bill += shopping_list[count][1]
    count += 1

print("Total       %d" % bill)




