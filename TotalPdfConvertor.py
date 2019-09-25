# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:23:41 2019

@author: AN389897
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 00:20:54 2019

@author: AN389897
"""

import os
from pdfConverter import pdf_to_text
from datetime import datetime
from ImageSupport import image_to_text

startTime = datetime.now()
class PdfConvertTool:
    stopper = True
    
    def pdf(self,filelist):
        pdf_object = list(map(lambda i : pdf_to_text(i),filelist))
        for l in range (0,len(pdf_object)):
            self.classifier(filelist[l],pdf_object[l])
    
    def classifier(self,filename,file):
        
        if self.stopper:
            print('************************************************')
            print(filename)
            print('------------------------------------------------')
        
        if len(file) > 2:
        # increase length here if your file has junk value in text like page number etc 
        #and important stuff as image in pdf
            self.stopper = True
            self.getclass(file)
        elif self.stopper:
            self.stopper = False
            self.classifier(filename,image_to_text(filename))
            #to convert the pdf if it is made of images, uses google tesseract
        else:
            self.stopper = True    
            pass 
        
    
    def getclass(self,t):
        print(t)
    
if __name__ == '__main__':
    file_pdf = [i for i in os.listdir() if i.endswith('.pdf')]
    
    pct = PdfConvertTool()
    pct.pdf(file_pdf)
    print(datetime.now() - startTime)
