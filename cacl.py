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






