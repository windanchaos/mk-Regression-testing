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
import sys
import os
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
api_address = ''
CONFIGFILE = os.getcwd() + '/aliyun.ini'
CONFIGSECTION = 'Credentials'
cmdlist = '''
接口说明请参照pdf文档
'''


def percent_encode(str):
    res = urllib.quote(str.decode(sys.stdin.encoding).encode('utf8'), '')
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res


def compute_signature(parameters, access_key_secret):
    sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])

    canonicalizedQueryString = ''
    for (k, v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode(k) + '=' + percent_encode(v)

    stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])

    h = hmac.new(access_key_secret + "&", stringToSign, sha1)
    signature = base64.encodestring(h.digest()).strip()
    return signature


def compose_url(user_params):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())

    parameters = { \
        'AccessKeyId': access_key_id, \
        'accesskeysecret': access_key_secret, \
        'Format': 'JSON', \
        'Version': '2015-01-09', \
        'SignatureVersion': '1.0', \
        'SignatureMethod': 'HMAC-SHA1', \
        'SignatureNonce': str(uuid.uuid1()), \
        'Timestamp': timestamp,\
        }

    for key in user_params.keys():
        parameters[key] = user_params[key]

    signature = compute_signature(parameters, access_key_secret)
    parameters['Signature'] = signature
    if api_address.lower().startswith('http') and api_address is not None:
        url = api_address + "/?" + urllib.urlencode(parameters)
    else:
        print("url should start with http or https ,yours is not right,check your url")
    return url


def make_request(user_params, quiet=False):
    url = compose_url(user_params)
    print url


def setup_credentials():
    config = ConfigParser.ConfigParser()
    try:
        config.read(CONFIGFILE)
        global access_key_id
        global access_key_secret
        access_key_id = config.get(CONFIGSECTION, 'accesskeyid')
        access_key_secret = config.get(CONFIGSECTION, 'accesskeysecret')
    except Exception, e:
        print traceback.format_exc()
        print("can't get access key pair, use config --id=[accesskeyid] --secret=[accesskeysecret] to setup")
        sys.exit(1)


if __name__ == '__main__':
    parser = OptionParser("%s -u https://api_url Param1=Value1 Param2=Value2\n" % sys.argv[0])
    parser.add_option("-u", "--url", action="store", dest="api_url", help="the api base url")

    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.print_help()
        sys.exit(0)

    user_params = {}
    idx = 1

    if sys.argv[1] == '-u':
        api_address = sys.argv[2]
        idx = 3
        setup_credentials()
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

    make_request(user_params)
