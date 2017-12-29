# -*- coding: utf-8 -*-

import os
import shutil
import oss2
import codecs


access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', '保密')

access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', '保密')

bucket_name = os.getenv('OSS_TEST_BUCKET', '保密')

endpoint = os.getenv('OSS_TEST_ENDPOINT', '保密')


# 确认上面的参数都填写正确了

# for param in (access_key_id, access_key_secret, bucket_name, endpoint):
#
#     assert '<' not in param, '请设置参数：' + param

# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行

bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

def dirlist(path, allfile):

    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile
files=dirlist('js',[])
for f in files:
    des=f.replace(os.sep, '/').decode('gb2312',errors='ignore')
    # print (des)
    # bucket.put_object_from_file(des, f)
    with open(f ,'rb') as fileobj:
        bucket.put_object(des, fileobj, )