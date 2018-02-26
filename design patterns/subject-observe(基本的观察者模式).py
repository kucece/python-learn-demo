#基本的观察者模式

class AbstractSubject(object):
    
    observeList=[]
    state=""
    
    def attach(self,abstractObserve):
        pass
    
    def detach(self,abstractObserve):
        pass
    
    def notifyAll(self):
        pass
    
    def notify(self,abstractObserve):
        pass
    
    def setState(self,state):
        pass

class AbstractObserve(object):
    
    def subscribe(self,abstractSubject):
        pass
    
    def unsubscribe(self,abstractObserve):
        pass
    
    def update(self,state):
        pass


class SubjectImpl(AbstractSubject) :
    
    def attach(self,abstractObserve):
        self.observeList.append(abstractObserve)
        pass
    
    def detach(self,abstractObserve):
        self.observeList.remove(abstractObserve)
        pass
    
    def notifyAll(self):
        for item in self.observeList:
            item.update(self.state)
        pass
    
    def notify(self,abstractObserve):
        abstractObserve.update(self.state)
        pass
    
    def setState(self,state):
        self.state=state
        self.notifyAll()
  
class ObserveImpl(AbstractObserve):
    
    def subscribe(self,abstractSubject):
        abstractSubject.attach(self)
        pass
    
    def unsubscribe(self,abstractObserve):        
        abstractSubject.detach(self)
        pass
    
    def update(self,state):       
        print(key+"---now state(""):"+state)        
        pass
  

suject = SubjectImpl()
observe = ObserveImpl()
observe.subscribe(suject)
suject.setState("new state")


##访问当前变量的键
##glo = globals()
##for key in glo.keys():
##    if glo[key] == self:
##        
                
