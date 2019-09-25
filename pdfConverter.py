# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:08:39 2019

@author: AN389897
"""
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO

def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(line_margin = 0.1, all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    device = TextConverter(manager, retstr)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    filepath.close()
    device.close()
    retstr.close()
    return str(text)


if __name__ == "__main__":
    text = pdf_to_text("TLXI-MAXS0300-201906-01-IN.pdf")
    print(text)