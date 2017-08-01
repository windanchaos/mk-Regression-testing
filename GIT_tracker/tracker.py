# -*- coding: UTF-8 -*-
import re,string

file_path = "/opt/github/ArhasMK/mk-imgr-webent/src/main/java/com/mk/trade/controller/TradeController.java"
read_file = open(file_path, 'r')
for line in read_file.readlines():
    # if ( re.search('public class*', line)):
    #     print (s)
    classObj = re.match(r'public class (.*?) .*', line, re.M | re.I)
    if ( classObj ):
        print (classObj.group(1))

    matchObj2 = re.search(r'public (.*?) .*?', line, re.M | re.I)
    if ( matchObj2 ):
        print (matchObj2.group())
        print (matchObj2.group(1))

read_file.close()