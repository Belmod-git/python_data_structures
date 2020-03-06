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


def toStr(n,base):
    str1 = '0123456789ABCDEF'
    # 比如0,1< 2
    if n < base:
        return str1[n]
    else:
        return toStr(n // base,base) + str1[n%base]


print(toStr(100,10))
print(toStr(1453,16))