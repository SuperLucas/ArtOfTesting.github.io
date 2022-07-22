# -*- coding: UTF-8 -*-
# 题目1：将给定的字符串'a=1, b=2, c=3',输出为{"a": "1", "b": "3", "c": "2"}
import json
# 给定的字符串s
s = 'a=1, b=2, c=3'
# 去除空格
s = s.replace(' ','')
# 定义结果字典
d1 = dict()
# 循环处理，以逗号切割字符串s
for s1 in s.split(','):
    # s1是 a=1这样的，再次以=切割得到左边的a和右边的1设置到字典
    arr = s1.split('=')
    # arr[0]是a，arr[1]是1
    d1[arr[0]] = arr[1]
# 打印字典
print(d1)
d2 = json.dumps(d1,ensure_ascii=False)
print(d2)