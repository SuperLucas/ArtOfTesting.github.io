# -*- coding:utf-8 -*-

# 1、再发一个带参数的 get 请求，如在博客园搜索：postman,url 地址为：https://zzk.cnblogs.com/s/blogpost?w=postman
# 2、请求参数：w=postman，可以单个传，可以以字典的形式传参:{"w": "postman"}
# 3、多个参数格式：{"key1": "value1", "key2": "value2", "key3": "value3"}


import requests
# 定义搜索参数
'''
#方法一：单个参数定义
w = 'postman' 
# 赋值参数
r = requests.request('get','https://zzk.cnblogs.com/s/blogpost',params=w)
'''

# 方法二：使用字典传参
param = {'w':'postman'}
# 发起get请求
r = requests.request('get','https://zzk.cnblogs.com/s/blogpost',params=param)

# 打印状态码
print(r.status_code)

# 打印URL
print(r.url)

# 打印返回文本
print(r.text)

'''
附录response返回的其他信息
1.response 的返回内容（content）还有其它更多信息
-- r.status_code #响应状态码
-- r.content #字节方式的响应体，会自动为你解码 gzip 和deflate 压缩
-- r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回 None
-- r.json() #Requests 中内置的 JSON 解码器，requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取
-- r.url # 获取 url
-- r.encoding # 编码格式，requests自动检测编码
-- r.cookies # 获取 cookie
-- r.raw #返回原始响应体-- r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
-- r.raise_for_status() #失败请求(非 200 响应)抛出异常
'''


