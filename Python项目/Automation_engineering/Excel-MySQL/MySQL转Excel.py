# -*- coding:utf-8 -*-
# @Author ： 秉烛爱好者
# @File : MySQL转Excel
# @Project : Automation_engineering
# @Time : 2022/9/114:45
# Github : https://github.com/SuperLucas/ArtOfTesting.github.io.git
# Gitee : https://gitee.com/SuperLucas/ArtOfTesting.github.io.git

# 在此处下方键入你的内容：


# 第一行代码就是首先创建数据库的连接。
# 我的mysql用户名是root，密码是211314，
# 因为这里我启动是启动的是本地的数据库服务，所以是localhost。
# 斜杠后面跟的是这个数据库的名称hong
# 第二行代码就是使用pandas的read_sql()查询mysql表department中的数据
# 第二行代码就是将查询出来的数据通过pandas的to_excel()写到本地
# 执行结果成功写入本地excel文件
# ——————————————————————————
# 需要执行的导入库：
# pip3 install pymysql
# pip3 install openpyxl
# pip3 install pandas
# ——————————————————————————
from sqlalchemy import create_engine
import pandas as pd
import openpyxl

# 创建数据库连接
engine = create_engine('mysql+pymysql://root:rootroot@localhost/studydemo')

# 读取mysql数据
db = pd.read_sql(sql='SELECT * FROM course_copy1', con=engine)

# 导出数据到excel
db.to_excel('E:\测试\部门数据.xlsx')
