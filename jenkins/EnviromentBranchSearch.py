# -*- coding: UTF-8 -*-
import sys
import os
import paramiko

class Server(object):
    """
    ip 服务器IP
    user 登录账户，需要前置ssh免密码登录
    port ssh登录的端口
    cmd 登录后要执行的命令，命令和名之间用';'隔开。
        example cmd = 'ls -l;ifconfig'
    """
    def __init__(self, ip,user,port):
        self.ip = ip
        self.user = user
        self.port = port

    def ssh(self, cmd, password):
        """公钥密钥登录"""
        '''ssh对象'''
        ssh_client = paramiko.SSHClient()
        '''指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，password为设定的密码，如无不用指定password参数'''
        key_ssh = paramiko.RSAKey.from_private_key_file(os.path.expanduser('~')+os.path.sep+'.ssh'+os.path.sep+'id_rsa')
        '''把要连接的机器添加到known_hosts文件中'''
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        '''连接服务器'''
        if password is None :
            ssh_client.connect(hostname=self.ip, port=self.port, username=self.user, pkey=key_ssh)
        else:
            ssh_client.connect(hostname=self.ip, port=self.port, username=self.user, password=password)
        stdin, stdout, stderr = ssh_client.exec_command(cmd)
        result = stdout.read()
        if not result:
            result = stderr.read()
        ssh_client.close()
#        print(result.decode())
        return result.decode()

servers_dict = {}

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

for envi in servers_dict:
    ip = servers_dict[envi][0]
    port = servers_dict[envi][1]
    user = servers_dict[envi][2]
    server = Server(ip, user, port)
    cmd="cd ArhasMK && git branch | grep '*'"
    result=server.ssh(cmd, None)
    print(envi, "branch is:", result)



