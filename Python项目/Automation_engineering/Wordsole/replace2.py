# -*- coding:utf-8 -*-
from docx import Document
import re

doc = Document(r"G:\提取测试.docx")
restr = '"(?:[^"])*"'

for p in doc.paragraphs:
    matchRet = re.findall(restr, p.text)
    for r in matchRet:
        p.text = p.text.replace(r, '“' + r[1:-1] + '”')
doc.save(r'G:\提取测试_修正3.docx')

