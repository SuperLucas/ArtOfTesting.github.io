# -*- coding:utf-8 -*-
import re
pattern = re.compile('“.*?“',re.S)
str = "“爱上了肯德基；奥施康定来看待。1”奥术大师多“爱上了肯德基；奥施康定来看待。2”"
a = pattern.findall(str)
print(a)
print(a[0])