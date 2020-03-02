"""
乱序字符串是指一个字符串指示另一个字符串的重新排列
前提：字符串由26个小写字母集合组成，长度相同
比如：python   ypthon    head   aedh
目的：
    写一个布尔函数（返回值是布尔值的函数）
    solutionsl（'abcd','dbca'）
"""

# 穷举法：排除。原因是如果字符串过长，就有相同字符串长度的循环

# 检查   第一个字符串是不是出现在第二个字符串中
# def solutionsl():
#     a = input(str('请输入第一个字符串'))
#     b = input(str('请输入第二个字符串'))
#     for i in range(len(a)):
#         if a[i] in b:
#             return True
#         else:
#             return False
# print(solutionsl())

def solutionsl(s1,s2):
    alist = list(s2)
    pos1 = 0
    flag = True

    while flag and pos1 < len(s1):
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 +1
        if found:
            alist[pos2] = None
            pos1 = pos1 +1
        else:
            flag = False
    return flag
print(solutionsl('abcd','dbca'))


def solutions2(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    # ord() 返回的是字符串在阿斯克码中的数字
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1


    count = 0   # 如果某个字符在s1和s2中出现的次数相同，那么count + 1
    flag = True

    while count < 26 and flag:
        if c1 [count] == c2 [count]:
            count = count + 1
        else:
            flag = False
    return flag
print(solutions2('aaaabbbbcccc','bbbbaaaacccc'))


# 排序和比较
def solutions3(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    # 排序    通常复杂度是O(n^2)  或者  O(logn)
    alist1.sort()
    alist2.sort()

    flag = True

    pos = 0

    while pos < len(s1) and flag:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            flag = False

    return flag

print(solutions3('aaaabbbbcccc','bbbbccccaaaa'))