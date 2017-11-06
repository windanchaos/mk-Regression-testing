# -*- coding: utf-8 -*-
'''学习使用urlib3，集合了大部分方法的使用Demo.by windanchaos'''
import urllib3

'''
You’ll need a PoolManager instance to make requests. 
This object handles all of the details of connection pooling and thread safety.
'''
http = urllib3.PoolManager()


# make a request use request()
# request() returns a HTTPResponse object
# HTTPResponse返回了http的表头headers\状态码status\实体data.
# 定义超时和重试次数
r1 = http.request('GET', 'http://www.baidu.com',timeout=4.0,retries=10)
r2 = http.request('GET', 'http://httpbin.org/robots.txt')

print(r1.status)
# headers 是header的dict
print(r1.headers)
print(r1.data)

print(r2.status)
print(r2.headers)
print(r2.data)

# 请求数据的组织,下面访问baidu，使用手机端的User-Agent组织请求报头,返回的data就是移动端的了
agent={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) \
    Version/9.0 Mobile/13B143 Safari/601.1'}
r3 = http.request('GET', 'http://www.baidu.com', headers=agent)
print(r3.data)

# post和put请求，需要自己encode请求的参数
from urllib import urlencode
import json
encoded_args = urlencode({'arg': 'value'})
url4 = 'http://httpbin.org/post?' + encoded_args
r4 = http.request('POST', url4)
print(json.loads(r4.data.decode('utf-8'))['args'])

# 当然如果是form数据，urllib3也可以帮你encode，如：
r5 = http.request('POST', 'http://httpbin.org/post', fields={'field': 'value'})
print(json.loads(r5.data.decode('utf-8'))['form'],r5.status)

# post json demo
data = {'attribute': 'value'}
encoded_data = json.dumps(data).encode('utf-8')
r6 = http.request('POST', 'http://httpbin.org/post', body=encoded_data, headers={'Content-Type': 'application/json'})
print(json.loads(r6.data.decode('utf-8'))['json'])


# post file and binary data
'''
For uploading files using multipart/form-data encoding you can use the same approach as Form data and specify 
the file field as a tuple of (file_name, file_data)
'''
with open('example.txt') as fp:
    file_data = fp.read()
r7 = http.request('POST','http://httpbin.org/post', fields={'filefield': ('example.txt', file_data, 'text/plain')})
json.loads(r7.data.decode('utf-8'))['files']


'''
For sending raw binary data simply specify the body argument. It’s also recommended to set the Content-Type header
'''
with open('example.jpg', 'rb') as fp:
    binary_data = fp.read()
r8 = http.request('POST','http://httpbin.org/post',body=binary_data,headers={'Content-Type': 'image/jpeg'})
json.loads(r8.data.decode('utf-8'))['data']

# 对ssl默认是不支持的。需要提供额外的配置或下载额外的包。

# log & Errors & Exceptions¶
'''
If you are using the standard library logging module urllib3 will emit several logs. 
In some cases this can be undesirable. 
You can use the standard logger interface to change the log level for urllib3’s logger
>>>logging.getLogger("urllib3").setLevel(logging.WARNING)

>>> try:
...     http.request('GET', 'nx.example.com', retries=False)
>>> except urllib3.exceptions.NewConnectionError:
...     print('Connection failed.')
'''
