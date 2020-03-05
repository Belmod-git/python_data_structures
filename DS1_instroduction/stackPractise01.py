# 栈抽象数据类型的底层实现采用什么？   List
# 确定列表的哪一段是顶部，然后使用append和pop来实现操作
# 假设列表的的尾部是栈的顶部元素，push


from pythonds.basic.stack import Stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty())
s.push(4)
s.push('lala')

print(s.peek())

s.push(True)
print(s.size())

print(s.isEmpty())

s.push(10.9)
print(s.pop())
print(s.pop())
print(s.size())


# ()匹配
def parChecker(symbolString):
# symbolString  假设"( () )"

    s = Stack()
    flag = True
    index = 0

    while index < len(symbolString) and flag:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                flag = False
            else:
                s.pop()
                print(s)
        index = index + 1

    if flag and s.isEmpty():
        return True
    else:
        return False

print(parChecker('(())'))
print(parChecker('((())'))


# {[()]}   (  [  )  ]
# 每一个开始的符号被压入栈，等待匹配结果
# 当出现结束符号的时候，必须检查栈顶部的开始符号是什么类型，如果两个符号不匹配，则字符串不匹配
# 整个字符串处理完并且栈为空，则字符串匹配


def parChecker(symbolString):
    s = Stack()
    flag = True
    index = 0

    while index < len(symbolString) and flag:
        symbol = symbolString[index]

        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                flag = False
            else:
                top = s.pop()
                start = '([{'
                end = ')]}'

                if not start.index(top) == end.index(symbol):
                    # index函数   根据括号里内容获取下标
                    flag = False

        index = index + 1

    if flag and s.isEmpty():
        return True
    else:
        return False

print(parChecker('([{}])'))
print(parChecker('([{}]]'))