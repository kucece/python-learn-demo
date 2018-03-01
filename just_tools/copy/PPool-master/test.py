import PPool

p_set = PPool.PPool()
print('Searching for available proxies...')
p_set.Search()
print(p_set.GetProxiesNum(), 'available proxies found.')
print('Get 5 random proxies:')
for i in range(1,6):
    print(i,': ',p_set.GetRandomProxy())
p_set.WriteToFile('p.json')
print('All Done')
