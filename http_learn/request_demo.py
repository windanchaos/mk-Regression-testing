# -*- coding: utf-8 -*-
'''学习使用requests，集合了大部分方法的使用Demo.by windanchaos'''
import requests

# we have a Response object called r. We can get all the information we need from this object.

r1 = requests.get('https://api.github.com/events')
# Response Content
print(r1.text)
print(r1.encoding)

# POST
r2 = requests.post('http://httpbin.org/post', data = {'key':'value'})
print (r2.status_code)
payload = {'key1': 'value1', 'key2': 'value2'}
r2 =requests.post("http://httpbin.org/post",data=payload)

url = 'http://httpbin.org/post'
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
r = requests.post(url, files=files)
r.text

# PUT, DELETE, HEAD and OPTIONS
r3 = requests.put('http://httpbin.org/put', data = {'key':'value'})
print (r3.status_code)
r4 = requests.delete('http://httpbin.org/delete')
print (r4.status_code)
r5 = requests.head('http://httpbin.org/get')
print (r5.headers)
r6 = requests.options('http://httpbin.org/get')

# Passing Parameters In URLs
payload = {'key1': 'value1', 'key2': 'value2'}
r7 = requests.get('http://httpbin.org/get', params=payload, timeout=3)

# Binary Response Content
r8 = requests.get('http://dynamic-image.yesky.com/640x-//uploadImages/leadimage/2014/266/55/QS4928ATRIR1_W.jpg')
print(r8.content)

# JSON Response Content
r9 = requests.get('https://api.github.com/events')
print(r9.json())

# raw socket response
r10 = requests.get('https://api.github.com/events', stream=True)
r10.raw
r10.raw.read(10)

# Custom Headers
'''
    Authorization headers set with headers= will be overridden if credentials are specified in .netrc, 
    which in turn will be overridden by the auth= parameter.
    Authorization headers will be removed if you get redirected off-host.
    Proxy-Authorization headers will be overridden by proxy credentials provided in the URL.
    Content-Length headers will be overridden when we can determine the length of the content.
'''
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r11 = requests.get(url, headers=headers)

# Cookies
url = 'http://example.com/some/cookie/setting/url'
r12 = requests.get(url)
print(r12.cookies['example_cookie_name'])

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r13 = requests.get(url, cookies=cookies)
r13.text

'''
Cookies are returned in a RequestsCookieJar, which acts like a dict but also offers a more complete interface, 
suitable for use over multiple domains or paths. Cookie jars can also be passed in to requests
'''
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r14 = requests.get(url, cookies=jar)
r14.text

# Redirection and History
'''
By default Requests will perform location redirection for all verbs except HEAD.
We can use the history property of the Response object to track redirection.
'''
r15= requests.get('http://github.com')
r15.status_code
r15.history