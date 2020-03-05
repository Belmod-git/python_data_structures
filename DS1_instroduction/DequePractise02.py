# class Deque:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def addFrtont(self,item):
#         self.items.append(item)

#     def addRear(self,item):
#         self.items.insert(0,item)

#     def removeFront(self):
#         return self.items.pop()

#     def removeRear(self):
#         return self.items.pop(0)

#     def size(self):
#         return len(self.items)


# s = input('')
# if not s:
#     print('请不要输入空字符串')
#     s = input('请输入一个新的字符串：')
# a = reversed(list(s))
# if list(a) == list(s):
#     print('是回文')
# else:
#     print('不是回文')


# from collections import deque
from pythonds.basic.deque import Deque

def palChecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)    # addRear 添加新项到deque尾部
    flag = True

    while chardeque.size() > 1:
        first = chardeque.removeFront()
        last = chardeque.removeRear()

        if first != last:
            flag = False

    return flag


print(palChecker('山西运煤车煤运西山'))
print(palChecker('上海自来水来自海上'))
print(palChecker('python'))