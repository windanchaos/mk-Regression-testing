# -*- coding: utf-8 -*-
'''学习使用requests，集合了大部分方法的使用Demo.by windanchaos'''
import requests
r = requests.get('https://api.github.com/events')
print(r.text)