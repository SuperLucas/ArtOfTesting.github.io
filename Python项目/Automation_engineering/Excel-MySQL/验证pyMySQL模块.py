# -*- coding:utf-8 -*-
# @Author ： 秉烛爱好者
# @File : 验证pyMySQL模块
# @Project : Automation_engineering
# @Time : 2022/9/115:17
# Github : https://github.com/SuperLucas/ArtOfTesting.github.io.git
# Gitee : https://gitee.com/SuperLucas/ArtOfTesting.github.io.git

# 在此处下方键入你的内容：
# pip3 install pymysql
import pymysql

user = input('user>>: ').strip()
pwd = input('password>>: ').strip()

# 建立链接
conn = pymysql.connect(
    host='192.168.0.103',  # 我的IP地址
    port=3306,  # 不是字符串不需要加引号。
    user='root',
    password='123',
    db='xing',
    charset='utf8'
)

# 拿到游标
cursor = conn.cursor()

# 执行sql语句

sql = 'select * from userinfo where user = "%s" and pwd="%s"' % (user, pwd)
print(sql)
res = cursor.execute(sql)
print(res)

cursor.close()
conn.close()

# 进行判断
if res:
    print('登录成功')
else:
    print('登录失败')