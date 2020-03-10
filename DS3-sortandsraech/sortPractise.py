'''
        [54,26,93,17,77,31,44,55,20]
第一趟  [26,54,93,17,77,31,44,55,20]   54和26交换
第二趟  [26,54,93,17,77,31,44,55,20]   为交换
第三趟  [26,54,17,93,77,31,44,55,20]   93和17交换
第四趟  [26,54,17,77,93,31,44,55,20]   93和77交换
第五趟  [26,54,17,77,31,93,44,55,20]
第六趟  [26,54,17,77,31,44,93,55,20]
第七趟  [26,54,17,77,31,44,55,93,20]
第八趟  [26,54,17,77,31,44,55,20,93]

列表中有n项，那第一遍比对需要n-1次，第二遍n-2

8遍   n-1遍

第二遍  [26,17,54,31,44,55,20,77,93]    n-2
第三遍  [17,26,31,44,20,54,55,77,93]
第四遍  [17,26,31,20,44,54,55,77,93]
第五遍  [17,26,20,31,44,54,55,77,93]
第六遍  [17,20,26,31,44,54,55,77,93]

'''

# a和b交换
# a = 10
# b = 20
# temp = a
# a = b
# b = temp
# print(a)
# print(b)


# def bubbleSort(alist):
#     flag = True
#     passnum = len(alist) - 1

#     while passnum > 0 and flag:
#         flag = False
#         for i in range(passnum):
#             if alist[i] > alist[i+1]:
#                 flag = True
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp

#         passnum = passnum - 1

# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)

'''
    选择排序
'''

# def selectionSort(alist):
#     for fillsort in range(len(alist)-1,0,-1):
#         maxpos = 0
#         for location in range(1,fillsort+1):
#             if alist[location] > alist[maxpos]:
#                 maxpos = location
#                 print(alist)

        # temp = alist[fillsort]
        # alist[fillsort] = alist[maxpos]
        # alist[maxpos] = temp

# alist = [54,26,93,17,77,31,44,55,20]
# selectionSort(alist)
# print(alist)


'''
插入排序
'''
# def insertionSort(alist):
#     for i in range(1,len(alist)):
#         currentValue = alist[i]
#         pos = i
#         while pos > 0 and alist[pos - 1]>currentValue:
#             alist[pos] = alist[pos - 1]
#             pos = pos - 1

        # alist[pos] = currentValue

# alist = [54,26,93,17,77,31,44,55,20]
# insertionSort(alist)
# print(alist)


'''
希尔排序
'''
# def shellSort(alist):
#     sublistcount = len(alist) // 2

    # while sublistcount > 0:
    #     for startposition in range(sublistcount):
    #         gapInsertionSort(alist,startposition,sublistcount)

        # print('alist:',alist)

    # sublistcount = sublistcount // 2

# def gapInsertionSort(alist,start,gap):
#     for i in range(start+gap,len(alist),gap):
#         currentValue = alist[i]

        # pos = i
        # while pos > 0 and alist[pos - 1] > currentValue:
        #     alist[pos] = alist[pos - gap]
        #     pos = pos - gap

        # alist[pos] = currentValue


# alist = [54,26,93,17,77,31,44,55,20]
# shellSort(alist)
# print(alist)


