# coding=utf-8

# from re import *
# from time import *
from threading import *

COMMON = 1
FULL = 2

poems = []


def thread1(library):
    global poems

    if library == COMMON:
        with open(r"Resource\CommonLibrary.txt", encoding="utf-8") as poemsFile:
            poemsString = poemsFile.read()

        for line in poemsString.split("\n"):
            line = line.split("\t")
            if len([0]) >= 5:  # 判断是否为诗句（而非诗题）
                poems.append(line[0])
    elif library == FULL:
        with open(r"Resource\FullLibrary.txt", encoding="utf-8") as poemsFile:
            poemsString = poemsFile.read()

        for poem in poemsString.split("\n\n"):
            poem = poem.split("\n")

            if len(poem[3]) <= 128:  # 判断是否为诗句（而非赏析）
                poems += poem[3].split("。")[: -1]


def thread2():
    word = input("请输入飞花令汉字：")
    deal = 0

    for poem in poems:
        if word in poem:
            deal += 1

            print(poem)

    print(f"\n共 {deal} 首诗！")


writer = Thread(target=thread1, args=(FULL,))
reader = Thread(target=thread2)

writer.start()
reader.start()
