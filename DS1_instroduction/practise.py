"""
问题描述：使用函数，求前n个整数的和
"""
import time

def sum(n):
    s = time.time()
    a = 0
    for i in range(1,n+1):
        a = a + i
    e = time.time()
    return a,e-s

print(sum(10000))

# 高斯函数
def sum2(n):
    return (n*(n+1))/2
s = time.time()
print(sum2(10000))
e = time.time()
print(e-s)


# def foo(lala):
#     a = 0
#     for b in range(1,lala+1):
#         c = b
#         a = a + c
#     return a
# print(foo(10))


# def one(a):
#     if a //2 == 0:
#         num = 0
#         i = 0
#         for e in range(1,a+1):
#             num = a-i+e
#             i+=1
#         return num
#     elif a // 2 != 0:
#         num = 0
#         i = 1
#         for e in range(1,a+1):
#             num = a-i+e
#             i+=1
#         return num