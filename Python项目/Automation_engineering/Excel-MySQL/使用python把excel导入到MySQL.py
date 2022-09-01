# -*- coding:utf-8 -*-
# @Author ： 秉烛爱好者
# @File : Excel导出
# @Project : Automation_engineering
# @Time : 2022/9/116:25
# Github : https://github.com/SuperLucas/ArtOfTesting.github.io.git
# Gitee : https://gitee.com/SuperLucas/ArtOfTesting.github.io.git

# 在此处下方键入你的内容：

# 使用python把excel导入到MySQL
import xlrd
import pymysql

# 打开数据所在的路径表名
book = xlrd.open_workbook('模拟数据.xls')
# 这个是表里的sheet名称
sheet = book.sheet_by_name('sheet1')

# 建立一个 MySQL连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='rootroot',
    db='studydemo',
    port=3306,
    charset='utf8'
)

# 获得游标
cur = conn.cursor()

# 创建插入sql语句
query = 'insert into course01(Cno,' \
        'Cname,Cr,)values(%s,%s,%s)'

# 创建一个for循环迭代读取xls文件每行数据的，
# 从第二行开始是要跳过标题行
# 括号里面1表示从第二行开始(计算机是从0开始数)
for r in range(1, sheet.nrows):
    # (r, 0)表示第二行的0就是表里的A1:A1
    Cno = sheet.cell(r, 0).value
    Cname = sheet.cell(r, 1).value
    Cr = sheet.cell(r, 2).value
    values = (Cno,Cname,Cr)
    # 执行sql语句
    cur.execute(query, values)

# close关闭文档
cur.close()
# commit 提交
conn.commit()
# 关闭MySQL链接
conn.close()
# 显示导入多少列
columns = str(sheet.ncols)
# 显示导入多少行
rows = str(sheet.nrows)
print('导入'+columns+'列'+rows+'行数据到MySQL数据库!')