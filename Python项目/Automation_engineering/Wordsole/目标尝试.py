# -*- coding:utf-8 -*-
# @Author ： 秉烛爱好者
# @File : 目标尝试
# @Project : Automation_engineering
# @Time : 2022/8/212:17
# Github : https://github.com/SuperLucas/ArtOfTesting.github.io.git
# Gitee : https://gitee.com/SuperLucas/ArtOfTesting.github.io.git

# 在此处下方键入你的内容：

# 目标1：输出每个双引号间的文本如“好家伙好看；后后加括号。”爱神的箭奥施“啊实；打实。”-->好家伙好看；后后加括号。
s = '“好家伙好看；后后加括号。”'
print(s)
slen = int(len(s))
mid= slen//2
print(type(mid))

print(len(s))
print(type(slen))

ALLlslen = s[1:mid]
Slain = s[mid:slen-1]
print(ALLlslen+ '\n' + Slain)

# 目标2：将文本写入docx文件换行输出-->
'''
好家伙好看；后后加括号。
啊实；打实。
'''


# 目标3：将文本再次在；后换行，并在docx输出
'''
好家伙好看；
后后加括号。
啊实；
打实。
'''


# 目标4：在原docx文件中实现
'''
好家伙好看；
后后加括号。
啊实；
打实。
'''


# 目标5：将上述文本在源文件中加粗
