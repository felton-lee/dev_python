#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : january13.py
@Author: lee
@Date  : 2020/1/7 6:42
@Desc  : 
'''
# int
print(int('0b100', base=2))
# float
print(float('1e+9'))
print(float('1e-6'))
a = 1.2e-4
print("%.5f" % a)
print("{:.5f}".format(a))
print(round(a, 5))
# 判断字符串是否是可迭代对象
from collections import Iterable, Iterator

b = '你好'
print(isinstance(b, Iterable))  # False
print(hasattr(str, '__iter__'))
myList = [11, 10, 1, 2, 9, 3, 8, 4, 5, ]
obj = reversed(myList)
print(hasattr(obj, '__next__'))  # True
# 生成器应用
print((i for i in range(10)))


def gen_obj(lst):
    for i in lst:
        a = yield i
        print("a is %s" % a)


g = gen_obj(myList)
# print(next(g))
g.__next__()
g.send(100)


# 序列协议
class Book:
    def __init__(self):
        self.book = ["红楼梦", "西游记", "金瓶梅"]

    def __getitem__(self, item):
        print("start Book-getitem func")
        return self.book[item]


b = Book()
for i in b:
    print(i)
print(b[2])  # 金瓶梅


class Person:
    def __init__(self):
        self.msg = {"name": "lee", "age": 24}

    def __iter__(self):
        for i in self.msg.items():
            yield i

    def __getitem__(self, item):
        print("start Person-getitem func")
        return self.msg[item]


p = Person()
for i in p:
    print(i)
print(p["name"])


# 迭代器实现可迭代对象
class MyIterator(Iterator):
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __next__(self):
        if self.index == len(self.lst):
            raise StopIteration
        city = self.lst[self.index]
        self.index += 1
        return self.getCityMsg(city)

    def getCityMsg(self, city):
        msg = "该%s的信息是...." % city
        return msg


class MyIterable(Iterable):
    def __init__(self, lst):
        self.iterator = MyIterator(lst)

    def __iter__(self):
        return self.iterator


iterable = MyIterable(["北京", "上海", "济南"])
for i in iterable:
    print(i)


# 生成器实现可迭代对象
class MyGenerator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in self.lst:
            yield self.getCityMsg(i)

    def getCityMsg(self, city):
        msg = "该%s信息是...." % city
        return msg


my_generator = MyGenerator(["上海", "济南", "北京"])
for i in my_generator:
    print(i)


# 生成器斐波那契数列

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


for i in fib(10):
    print(i)

f = fib(6)
while True:
    try:
        value = next(f)
        print(value)
    except StopIteration as e:
        print(e.value)
        break
