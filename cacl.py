#coding:utf-8

from itertools import permutations


def recursion(res,ops):
    if len(res[0]) == 1:
        #递归结束
        return res
    else:
        result = []

        for r in res:
            exlucedict = dict()
            #A4,2 取出A4,2，A3,2 A2,2的排列然后迭代
            a42 = list(permutations(r,2))
            for i in a42:
                for op in ops:
                    tmp = r[:]
                    tmp.remove(i[0])
                    tmp.remove(i[1])
                    exp_1 = "(" + i[0] + op + i[1] + ")"
                    exp_2 = "(" + i[1] + op + i[0] + ")"

                    if op not in ["*","+"]:
                        #过滤数字相同时 / - 表达式中的排列产生的重复
                        if not exlucedict.get(exp_1):
                            exlucedict[exp_1] = 1
                            tmp.append(exp_1)
                            result.append(tmp)
                        continue

                    # #去重 + *
                    if exlucedict.get(exp_1) == None and exlucedict.get(exp_2) == None:
                        exlucedict[exp_1] = 1
                        tmp.append(exp_1)
                        result.append(tmp)


    # del exlucedict
    return recursion(result, ops)


def main():
    number = [["5", "5", "6", "6"]]
    #number = [["3", "8", "4", "6"]]
    #number = [["2", "7", "3", "4"]]

    ops = ["+", "-", "*", "/"]

    answer = 24
    result = recursion(number, ops)
    result2 = list()
    for i in result:
        try:
            if eval(i[0]) == answer:
                result2.append(i[0])
        except:
            pass

    if len(result2) > 0:
        for j in result2:
            print j
    else:
        print u"无解"


if __name__ == "__main__":
    main()

##实现的功能##
#可以支持n个数，加减乘除运算，等于任何结果。不只是4个整数，24
#由于整数的除法除不尽的时候会去向下去整（golang也会），所以得出的表达式会比用浮点数多


##方法##
#类似于分治的方式依次解决二元运算，将四元运算分成三次二元运算
# 加减乘除都是二元运算符，首先将长度为n的数组根据排列的两两结合变成n-1数组，然后递归，变成n-2,n-3
#当n-m = 1时递归结束。在遍历的过程中将“*”，“+”判断是否出现过（或者交换出现过）没有就放入下一次的递归，有就pass
#这样就枚举出所有组合了，然后求值，打印出结果等于answer的所有表达式，pass掉所有不等于answer或者错误的表达式（例如4/0）

##递归==
#递归调用的次数n-1(n为参加计算的整数个数），时间复杂度不算高，压栈可控

##python##
#1.python math包已经实现了排列组合的函数
#2.python 的反射eval能将字符串映射到上下文（上文）中出现的对象
#这两点可以减少很多工作量和代码量




