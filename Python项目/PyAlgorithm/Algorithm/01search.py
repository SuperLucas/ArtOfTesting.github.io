# coding=utf-8
# 中文注释
#二分查找算法：猜数字

# 定义search函数，list[]为此数组，item为正确答案，为常量固定值
def search(list,item):
    #定义跟踪查询的列表最小值
    low = 0
    #定义跟踪查询的列表最大值
    high = len(list)-1

    #设计循环，当最小值≤最大值，即中间还有数字时，可查询，否则返回none
    while low <= high:
        #二分查找中位数算法
        mid = (low+high)/2
        #设定二分查找的数字必定为中位数
        guess = list[mid]

        #分支1：若查找数字等于结果值item
        if guess == item:
            return mid
        #分支2：若查找数字小于结果值，则最小值low=二分查找数+1
        if guess < item:
            low = mid + 1
        #分支3：若查找数字小于结果值，则最大值high=二分查找数-1
        else:
            high = mid -1
    return none

my_list = [1,3,5,7,9]


