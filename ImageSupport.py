# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:31:34 2019

@author: AN389897
"""
from PIL import Image
import pytesseract
from wand.image import Image as Img
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\an389897\AppData\Local\Tesseract-OCR\tesseract.exe"

def image_to_text(file_name):
    text = ''
    with Img(filename=file_name, resolution=300) as img:
        img.compression_quality = 99
        img.save(filename= file_name[:-4]+'.jpg')
        
    total_image_file = [i for i in os.listdir() if i.endswith('.jpg')]
    for image in total_image_file:
        text += pytesseract.image_to_string(Image.open(image))
        os.remove(image)
    
    print(text[0:100])
    return text