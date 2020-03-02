import time

# 拼接
def test1():
    list1 = []
    for i in range(1000):
        list1 = list1 + [i]


# append 方式
def test2():
    list1 = []
    for i in range(1000):
        list1.append(i)


# 列表推导式
def test3():
    list1 = [i for i in range(1000)]


# 强转列表
def test4():
    list1 = list(range(1000))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()

t1 = Timer('test1()','from__main__import test1')
print(t1.timeit(number=1000))