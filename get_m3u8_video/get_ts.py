# coding=utf8
import requests

url='https://sina.com-h-sina.com/20180906/18215_c0fc8873/800k/hls/f997a136b73'

for i in range(0,675):
    f = open("E:/Downloads/tmp/%03d.ts" % i, 'wb')
    data = requests.get(url + str(i).zfill(3) + '.ts')
    f.write(data.content)
    f.close()
    print('ts %03d OK' % i)