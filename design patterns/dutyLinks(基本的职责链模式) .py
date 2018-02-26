#基本的职责链模式

class handler(object):
    nextHandler = None

    def setNextHandler(self,handler):
        self.nextHandler = handler
        pass


#职责链嵌套
#职责链怎么通过数据驱动的形式进行动态的重组职责链的顺序，单一直链还是树状链，有向无环图
#如果是直链的话，此处可使用装饰器进行切面编程
    def handlerRequest(self,request):
        #dosomething
        if self.nextHandler is None:
            return True
        return self.nextHandler.handlerRequest(request)
        pass


class handler_one(object):
    nextHandler = None

    def setNextHandler(self,handler):
        self.nextHandler = handler
        pass

    def handlerRequest(self,request):
        #dosomething
        print("request < 500",request < 500)
        if request < 500:
            return False
        if self.nextHandler is None:
            return True
        return self.nextHandler.handlerRequest(request)
        pass


class handler_two(object):
    nextHandler = None

    def setNextHandler(self,handler):
        self.nextHandler = handler
        pass

    def handlerRequest(self,request):
        #dosomething    
        print("request < 5000",request < 5000)
        if request < 5000:
            return False
        if self.nextHandler is None:
            return True
        return self.nextHandler.handlerRequest(request)
        pass
#python3 怎么才能动态进行类实例化对象
handler_list = []
gobals_dict = dict(globals().items())
for key in gobals_dict.keys():
    print("class","class" in str(gobals_dict[key]))
    if key.startswith("handler_") and "class" in str(gobals_dict[key]):
        print(key)
        print("append:",key)
        handler_list.append(key)
        
request = 501
start = handler()
pre = start
print(handler_list)
##handler_list.reverse()
print(handler_list)
for item in handler_list:
    print(item+"()")
    now = eval(item+"()")
    pre.setNextHandler(now)
    pre = now
start.handlerRequest(request)
    
