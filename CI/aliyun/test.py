#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
处理拼接阿里云api的url。
阿里云api的url构成：

    产品api的url+api的请求参数+公共参数

    example:
        cdn request url:
            https://cdn.aliyuncs.com/?Action=RefreshObjectCaches&ObjectType=File&ObjectPath=example.com&SignatureVersion=1.0&Format=JSON&TimeStamp=2018-01-24T08%3A55%3A18Z&&AccessKeyId=scret&SignatureMethod=HMAC-SHA1&Version=2014-11-11&Signature=secret%3D&SignatureNonce=4d93418c-00e4-11e8-a82b-00163e000306
            产品api的url:https://cdn.aliyuncs.com/
            api的请求参数:Action=RefreshObjectCaches&ObjectType=File&ObjectPath=example.com
            公共参数:SignatureVersion=1.0&Format=JSON&TimeStamp=2018-01-24T08%3A55%3A18Z&&AccessKeyId=scret&SignatureMethod=HMAC-SHA1&Version=2014-11-11&Signature=secret%3D&SignatureNonce=4d93418c-00e4-11e8-a82b-00163e000306

    api详情参考阿里云产品文档

"""
import sys, os
import urllib, urllib2
import base64
import hmac
import hashlib
from hashlib import sha1
import time
import uuid
import json
from optparse import OptionParser
import ConfigParser
import traceback

access_key_id = ''
access_key_secret = ''
api_address = 'https://cdn.aliyuncs.com'
CONFIGFILE = os.getcwd() + '/aliyun.ini'
CONFIGSECTION = 'Credentials'
cmdlist = '''
接口说明请参照pdf文档
'''

if __name__ == '__main__':
    parser = OptionParser("%s url=api_url Param1=Value1 Param2=Value2\n" % sys.argv[0])
    parser.add_option("-i", "--id", dest="accesskeyid", help="specify access key id")
    parser.add_option("-s", "--secret", dest="accesskeysecret", help="specify access key secret")
    parser.add_option("-u", "--url", action="store", dest="api_url", help="the api base url")

    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.print_help()
        sys.exit(0)

    user_params = {}
    idx = 1

    if not sys.argv[1] is '-u':
        user_params['api_url'] = sys.argv[2]
        idx = 3
    else:
        parser.print_help()
        sys.exit(0)

    for arg in sys.argv[idx:]:
        try:
            key, value = arg.split('=')
            user_params[key.strip()] = value
        except ValueError, e:
            print(e.read().strip())
            raise SystemExit(e)
