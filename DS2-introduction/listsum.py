'''
[1,3,5,7,9]
'''


# def listsum(numList):
#     sum = 0
#     for i in numList:
#         sum = sum + i

    # return sum


# print(listsum([1,3,5,7,9]))


# 不能使用while或者for
# 使用小学的内容：连加
#  （1+ (3+ (5+ (7+ (9)))))


# def ListSum2(numList):   # 递归函数，调用自身的函数
#     if len(numList) == 1:
#         return numList[0]
#     else:
#         return numList[0] + ListSum2(numList[1:])


# print(ListSum2([1,3,5,7,9]))


# def toStr(n,base):
#     str1 = '0123456789ABCDEF'
#     # 比如0,1< 2
#     if n < base:
#         return str1[n]
#     else:
#         return toStr(n // base,base) + str1[n%base]   # 将递归调用的结果和str1的字符串拼接


# print(toStr(100,10))
# print(toStr(1453,16))


# 栈实现递归
from pythonds.basic.stack import Stack

rStack = Stack()

def toStr(n,base):
    convertString = '0123456789ABCDEF'

    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n%base])

        n = n // base

    res = ''
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res
print(toStr(1453,16))