#! /usr/bin/env python
# coding:utf-8
##自动注册模板
import requests
import os
import execjs
import logging
import json
import time
import sys
import random
import cv2

from PIL import Image
import pytesseract

class AutoReg(object):

    login_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'}
    signin_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest', 
		'Content-Length': 0, 
		'Origin': 'http://www.XXXX.com/',
        'Referer': 'http://www.XXXXX/register.html'}
    phone = ''



    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename="auto_get_flow.log",
                        filemode='a')
   
    def __init__(self):
        
        pass

    def start(self):
        
        self.s = requests.Session()
        pass

    def stop(self):
        
        self.s.close()

    def getCode(self):
        self.imageId = str(random.random())
        resp =  self.s.get(url='http://www.XXXXX.com/captcha/image?imageId='+self.imageId, headers=self.login_header)
        with open("temp.jpg", "wb") as code:
           code.write(resp.content)
##方法一：手动
##        img = cv2.imread("temp.jpg")
##        cv2.imshow("code",img)
##        cv2.waitKey(25)
##        self.code = input("input code:")
##        cv2.destroyAllWindows()
##方法一：调用 tesseract 识别       
        pre_pwd=os.getcwd()
        imageObject=Image.open('temp.jpg').convert("L")
        os.chdir(os.path.join(pre_pwd+"\\Tesseract-OCR"))
        self.code = pytesseract.image_to_string(imageObject)
        print(self.code)
        os.chdir(pre_pwd)
        

    def reg(self,userName=None,dafault=True):
        print ('reg...')
        #注册信息
        if dafault == True:
            self.userType="1"
            self.userName="XXXXX"
            self.userPassword="XXXXX"
            self.confirmPassword="XXXXX"
            self.qq="XXXXX"
            self.email="XXXXX@qq.com"
            self.questionId="4"
            self.answer="XXXXX"
        if userName is not None:
            self.userName=userName
            
        postdata={
            "userType":self.userType,
            "userName":self.userName,
            "userPassword":self.userPassword,
            "confirmPassword":self.confirmPassword,
            "qq":self.qq,
            "email":self.email,
            "questionId":self.questionId,
            "answer":self.answer,
            "code":self.code,
            "imageId":self.imageId
            }
        resp =  self.s.post(url='http://www.XXXXX.com/registerForm',params=postdata, headers=self.login_header)
        result =resp.text
        print(result)     
        
        data = json.loads(result)        
        if data['code'] == '111':
            print (self.userName)
            print ("postdata:",postdata)
            print ("returndata:",result)
            print("success")
            print("success==================",self.userName)
        else:
            print (self.userName)
            print ("postdata:",postdata)
            print ("returndata:",result)
            print("fail")

#{"code":"002","data":null,"msg":"验证码错误"}
#{"code":"029","data":null,"msg":"今日注册次数过多"}
#{"code":"111","data":null,"msg":"注册成功"}

if __name__ == '__main__':

    for i in range(5):            
        user = AutoReg()
        user.start()
        user.getCode()
        user.reg(userName="qazqwe08"+str(i))
        user.stop()

    
