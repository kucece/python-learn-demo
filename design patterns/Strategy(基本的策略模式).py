import subprocess
import os
import time

class AbstractStrategy(object):
    def surfing(self,context):
        pass
class AbstractSurfingStrategy(AbstractStrategy):
    strategy=None

    def setSurfingStrategy(self,strategy):
        self.strategy = strategy
        pass
    def surfing(self,context):
        print(context,"上网")
        self.strategy.surfing(context)
        pass
class SurfingStrategyOnIphone(AbstractStrategy):
    def surfing(self,context):
        print(context,"苹果上网")
        pass
class SurfingStrategyOnPC(AbstractStrategy):
    def surfing(self,context):
        print(context,"电脑上网")
        pass
    
class SurfingStrategyOnAndroid(AbstractStrategy):
    def surfing(self,context):
        print(context,"安卓上网")
        pass
class SurfingStrategyOnWeb(AbstractStrategy):
    def surfing(self,context):
        print(context,"web上网")
        pass



if __name__ == '__main__':
    context = "我"
    demo = AbstractSurfingStrategy()
    ##策略的指定可以交由配置文件来指定，通过读取配置文件来实例具体策略。避免了反复修改源码    
    demo.setSurfingStrategy(SurfingStrategyOnWeb())
    demo.surfing(context)
    demo.setSurfingStrategy(SurfingStrategyOnPC())
    demo.surfing(context)
    demo.setSurfingStrategy(SurfingStrategyOnIphone())
    demo.surfing(context)
    demo.setSurfingStrategy(SurfingStrategyOnAndroid())
    demo.surfing(context)
