#!/usr/bin/env python3

import builtwith as bw
import urllib3 as ul3



http = ul3.PoolManager()
try:
    r = http.request('GET', 'https://www.jd.com',timeout=4.0)
except ul3.exceptions.NewConnectionError:
    print('Connection failed.')

print (r.status)
#print (r.data.decode('utf-8'))
with open('baidu.html','a') as haha:
    haha.write(r.data.decode('utf-8'))