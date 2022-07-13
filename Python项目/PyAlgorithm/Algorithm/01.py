# coding=utf-8
# 中文注释
#二分查找算法：猜数字

# 1、定义search函数，list[]为此数组，item为正确答案，为常量固定值
# ！！！！注意空格！！！！！

def binary_search(list,item):
    # 2、定义跟踪查询的列表最小值、最大值
  low = 0
  high = len(list) - 1

    # 3、设计循环，当最小值≤最大值，即中间还有数字时，可查询，否则返回none
  while low <= high :
      # 4、二分查找中位数算法、设定二分查找的数字必定为中位数
    mid = (low + high) // 2
    guess = list[mid]

      # 5、分支1：若查找数字等于结果值item
    if guess == item:
      return mid
      # 6、分支2：若查找数字小于结果值，则最大值high=二分查找数-1
    if guess < item:
      high = mid - 1
      # 7、分支3：若查找数字小于结果值，则最小值low=二分查找数+1
    else:
      low = mid + 1
  # 8、返回None
  return None

# 9、定义一个数组
my_list = [1,3,5,7,9,2]

# 10、print输出时，3.0以后需要加(),注意输出时以0作为开始序号，所以元素2为第6位，而输出为5
print (binary_search(my_list,2)) # ==> 5
print (binary_search(my_list,-1)) # => None