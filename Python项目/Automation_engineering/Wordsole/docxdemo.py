
# https://blog.csdn.net/ityouknow/article/details/105236575
from docx import Document
import re

doc = Document(r"G:\对联话demo.docx")
restr = '“(?:[^“])*”'

for p in doc.paragraphs:
    matchRet = re.findall(restr, p.text)
    for r in matchRet:
        p.text = p.text.replace(r, '/n' + r[1:-1] + '/n')
doc.save(r'G:\对联话demo_1.docx')