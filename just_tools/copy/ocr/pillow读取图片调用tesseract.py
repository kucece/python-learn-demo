import time
import urllib.request

from PIL import Image
import pytesseract
import cv2
import os




pre_pwd=os.getcwd()
imageObject=Image.open('temp.jpg').convert("L")
print (imageObject)
os.chdir(os.path.join(pre_pwd+"\\Tesseract-OCR"))
print (pytesseract.image_to_string(imageObject))
print (len(pytesseract.image_to_string(imageObject)))
  
    
