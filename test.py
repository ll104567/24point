#coding=utf8
# import unittest

from itertools import permutations
from cacl import recursion
import random

class Test24Cacl(object):
    def __init__(self, numbers, ops,m,answer):
        self.numbers = numbers
        self.ops = ops
        self.m = m
        self.answer = answer

    def test_permut(self):
        ##测试排列
        for i in xrange(self.m,0, -1):
            print list(permutations(self.numbers,i))

    def test_recursion(self):
        result = recursion([self.numbers], ops)
        result2 = list()
        for i in result:
            try:
                if eval(i[0]) == self.answer:
                    result2.append(i[0])
            except:
                pass

        if len(result2) > 0:
            for j in result2:
                print j
        else:
            print u"无解"





if __name__ == '__main__':

    ops = ["+","-","*","/"]
    numbers = ["6", "2", "6", "2"]
    m = 2
    answer = 24

    #随机正整数
    #numbers = ["%s"%random.randint(1,100),"%s"%random.randint(1,100),"%s"%random.randint(1,100),"%s"%random.randint(1,100)]
    #print numbers


    #answer随机
    #answer = random.randint(1,100)
    #print answer

    #ops增加

    cal = Test24Cacl(numbers,ops,m, answer)
    #cal.test_permut()
    cal.test_recursion()