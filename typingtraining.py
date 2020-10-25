# -*- coding = utf-8 -*-
# @Time: 2020/4/21  19:52
# @Author: GZL
# @File: typingtraining.py
# @Software: PyCharm

import random

def letter():
    letter ="abcdefghijklmnopqrstuvwxyz"
    i = len(letter)
    print(i)
    while 1:
        num = random.randint(0, i-1)
        tar = letter[num]
        print(tar)
        c_tar = input("repeat")
        if tar ==c_tar:
            continue
        else:
            print("-"*10+"nope you wrong"+"-"*10)


def words():
    words = ["print", "def", "while", "bs", "url", "urllib", "else", "continue", "break", "head", "body", "href", "if"]
    l = len(words)
    num = 






if __name__ == '__main__':
    print("1.letter   2.words")

    choice = int(input("number is _____"))

    if choice == 1:
        letter()
    elif choice == 2:
        words()
