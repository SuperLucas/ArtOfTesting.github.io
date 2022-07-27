# -*- coding:utf-8 -*-
import requests

# 1、将安装好的requests模块导入后，通过GET访问一个URL地址的网页页面，如：https://www.cnblogs.com/
# 2、这里的 r 也就是 response，请求后的返回值，可以调用 response 里的 status_code 方法查看状态码
# 3、状态码 200 只能说明这个接口访问的服务器地址是对的，并不能说明功能 OK，一般要查看响应的内容，r.text 是返回文本信息

# ！！！！！点击Ctrl，鼠标放在request上可查看Api.py文件！！！！！

# 使用requests，发起get无参数请求，请求博客园首页
r = requests.request('get','https://www.cnblogs.com/')

# 打印状态码
print(r.status_code)

# 打印返回文本
print(r.text)

