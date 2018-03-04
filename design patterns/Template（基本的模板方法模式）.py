import subprocess
import os
import time

class AbstractEatTemplate(object):
    #具体方法
    def step1(self):
        print("step1")
        print("book ticket")
    #抽象方法
    def step2(self):
##        print("step2")
##        print("order what to eat?")
        pass
    #具体方法
    def step3(self):
        print("step3")
        print("eating")
        pass
    #钩子方法
    def isDoStep4(self):
        print("is do step4")
        print("not to do")
        return False
    def step4(self):
##        print("step4")
##        print("what to do?")
        pass
    def doSeries(self):
        self.step1()
        self.step2()
        self.step3()
        if self.isDoStep4():
            self.step4()

class eat1(AbstractEatTemplate):
    def step2(self):
        print("step2")
        print("i want eat fish")
        print("i want eat rice")

class eat2(AbstractEatTemplate):
    def step2(self):
        print("step2")
        print("i want eat fish")
        print("i want eat rice")
    
    #钩子方法
    def isDoStep4(self):
        print("just do step4")
        return True
    
    def step4(self):
        print("step4")
        print("pack  and take away")




if __name__ == '__main__':
    demo = eat1()
    demo.doSeries()
    print("==============================")
    demo = eat2()
    demo.doSeries()
