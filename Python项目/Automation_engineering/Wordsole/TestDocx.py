# -*- coding:utf-8 -*-
from docx import Document
document = Document()
paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
prior_paragraph = paragraph.insert_paragraph_before('Lorem ipsum')
document.save(r"G:\test.docx")