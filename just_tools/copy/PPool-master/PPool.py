import urllib.request
from bs4 import BeautifulSoup
import re
import time
import random
import json


def _GetResponse(url):
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
        resp = urllib.request.urlopen(req, timeout=5)
        content = resp.read()
        return content

def _GetProxiesFrom_XiciDaili():
    res = []
    for i in range(1,2,1):
        url = 'http://www.xicidaili.com/wn/' + str(i)
        html = _GetResponse(url)
        soup = BeautifulSoup(html, 'html5lib')
        trs = soup.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if tds == []:
                continue
            proxy = dict()
            proxy[tds[5].contents[0].lower()] = tds[1].contents[0] + ':' + tds[2].contents[0]
            res.append(proxy)
    return res
            
class PPool:
    def __init__(self):
        self.__pool = []
    
    def CheckAlive(self, proxy):
        try:
            resp=0
            proxy_support = urllib.request.ProxyHandler(proxy)
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
            req = urllib.request.Request('http://www.qq.com', headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
            resp = urllib.request.urlopen(req, timeout=5)
            if resp.code == 200:
                return True
        except Exception as e:
            print(e)
        return False

    def Search(self, finder = _GetProxiesFrom_XiciDaili):
        temp = finder()
        for proxy in temp:
            if self.CheckAlive(proxy):
                self.__pool.append(proxy)

    def ReCheckAliveAll(self):
        for proxy in self.__pool:
            if not self.CheckAlive(proxy):
                self.__pool.remove(proxy)
        
    def GetRandomProxy(self):
        return random.choice(self.__pool)

    def GetProxiesNum(self):
        return len(self.__pool)

    def WriteToFile(self,pathname = 'proxies.json'):
        with open(pathname, 'w') as file_obj:
            json.dump(self.__pool, file_obj)

    def LoadFromFile(self,pathname = 'proxies.json'):
        with open(pathname, 'r') as file_obj:
            self.__pool = json.load(file_obj)

