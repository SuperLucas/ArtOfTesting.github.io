# -*- coding:utf-8 -*-
# @Author ： 秉烛爱好者
# @File : 选择排序
# @Project : PyAlgorithm
# @Time : 2022/8/1717:54
# Github : https://github.com/SuperLucas/ArtOfTesting.github.io.git
# Gitee : https://gitee.com/SuperLucas/ArtOfTesting.github.io.git

# 在此处下方键入你的内容：
# 函数findSmallest：找到数组中的最小值
def findSmallest(arr):
    # 储存最小的值
    smallest = arr[0]
    # 储存最小的元素索引
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# 数组排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # 找到这个最小值，并按顺序放到另一个新数组中
        smallest = findSmallest(arr)
        # pop() 参数为列表元素的索引值,pop()方法有返回值,返回的是列表对应的元素.
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
