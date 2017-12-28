# -*- coding: utf-8 -*-

import os
import shutil
import oss2
import codecs

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
    des=f.replace(os.sep, '/')
    # print (des)
    # bucket.put_object_from_file(des, f)