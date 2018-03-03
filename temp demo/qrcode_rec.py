#用摄像头捕获视频，并以灰度图显示（也可以RGB）

# -*- coding: utf-8 -*-


#! /usr/bin/python
# -*- coding: utf8 -*-
# The QR reader module to decode QR codes.
#




"""
Created on Fri Jan 3 21:06:22 2014
@author: duan
"""
import numpy as np
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    
    
    #cvCopy(frame,gray);
    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imwrite('temp.png',frame)
    demo = decode(Image.open('temp.png'))
    
    print(len(demo))
    if len(demo) != 0:
##        data = demo.data.encode('utf-8')
        print(demo)
    #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

