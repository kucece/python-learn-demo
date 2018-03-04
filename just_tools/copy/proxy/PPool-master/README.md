# PPool 使用说明
自动抓取可用代理的工具。代理池。Proxies Pool。
默认代理都是从 http://www.xicidaili.com/ 上抓取的Https代理。
抓回的代理会使用qq.com进行测试，剔除不可用的。

## 使用方法

直接运行test.py脚本就会抓取大量代理保存在当前目录的proxies.json文件中。 单线程抓取验证，耗时比较长。

程序中使用如下：
```python
import PPool

p_set = PPool.PPool()
p_set.Search()
print(p_set.GetProxiesNum(), 'proxies found.')
for i in range(1,6):
    print(i,': ',p_set.GetRandomProxy())
p_set.WriteToFile('p.json')
```

## 修改
修改_GetProxiesFrom_XiciDaili()以修改抓取数量之类的东西。
或者仿照这样写一个函数_GetProxiesFrom_xxx()抓取其他来源的代理。
```python
p_set.Search(finder = _GetProxiesFrom_xxx())
```
