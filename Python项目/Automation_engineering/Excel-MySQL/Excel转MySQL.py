# -*- coding:utf-8 -*-
# @Author ： 秉烛爱好者
# @File : Excel转MySQL
# @Project : Automation_engineering
# @Time : 2022/9/114:48
# Github : https://github.com/SuperLucas/ArtOfTesting.github.io.git
# Gitee : https://gitee.com/SuperLucas/ArtOfTesting.github.io.git

# 在此处下方键入你的内容：

# 第一行代码就是首先创建数据库的连接
# 第二行代码使用pandas的read_excel()读取本地文件
# 第三步使用pandas的to_sql()方法将读取到的数据写入到mysql中
# 代码执行完成后返回mysql中我的hong数据库发现多出了一个test_data的表。


from sqlalchemy import create_engine
import pandas as pd

# 创建数据库连接
engine = create_engine('mysql+pymysql://root:rootroot@localhost/studydemo')

# 读取xlsx文件
df = pd.read_excel('E:\测试\模拟数据.xlsx')

# 导入到mysql数据库
df.to_sql(name='test_data', con=engine, index=False, if_exists='replace')