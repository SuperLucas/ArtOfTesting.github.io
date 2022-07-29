# -*- coding:utf-8 -*-
#


import docx
doc = docx.Document('my_template.docx')
for paragraph in doc.paragraphs:
    tmp = ''
    runs = paragraph.runs
    for i, run in enumerate(runs):
        tmp += run.text # 合并run字符串
        if '需要替换的字符串' in tmp:
            # 如果存在匹配得字符串，那么将当前得run替换成合并后得字符串
            run.text = run.text.replace(run.text, tmp)
            run.text = run.text.replace('需要替换的字符串', '我是替换后的字符串')
            tmp = ''
        else:
            # 如果没匹配到目标字符串则把当前run置空
            run.text = run.text.replace(run.text, '')
        if i == len(runs) - 1:
            # 如果是当前段落一直没有符合规则得字符串直接将当前run替换为tmp
            run.text = run.text.replace(run.text, tmp)
