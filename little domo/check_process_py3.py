import threading
import time
import os
import subprocess
#定时监控进程状态，如存在，则继续监控，如不存在，则启动目标进程
def get_process_count(imagename):
    p = os.popen('tasklist /v | find "'+imagename+'"  | find "'+os.getcwd()+'"')
    return p.read().count(imagename)
def watch_func(imagename,imagepath):
    if get_process_count(imagename) == 0 :
        print("run")
        print (os.system(imagepath))
if __name__ == "__main__":    
    print("start")
    print(os.getcwd())
    while True:
        print(os.path.join((os.getcwd()+'\client.exe').replace("\\","\\\\")))
        watch_func("client.exe",os.path.join(os.getcwd()+'\client.exe'))
        time.sleep(5)
        print("running")
        
