# -*- coding:utf-8 -*-
import os,random,subprocess
from shutil import copy2,rmtree,copytree,make_archive,move
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

    def ssh(self,cmd,password):
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
        print(result.decode())

    def sftp(self,password,local_file=os.path.expanduser('~')+os.path.sep+'sites.tar.gz',remote_path='/arthas/'+'sites.tar.gz'):
        """公钥密钥登录"""
        '''指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，password为设定的密码，如无不用指定password参数'''
        key_sftp = paramiko.RSAKey.from_private_key_file(
            os.path.expanduser('~') + os.path.sep + '.ssh' + os.path.sep + 'id_rsa')
        '''实例化一个trans对象# 实例化一个transport对象'''
        trans = paramiko.Transport((self.ip, self.port))
        if password is None:
            trans.connect(username=self.user, pkey=key_sftp)
        else:
            trans.connect(username=self.user, password=password)
        '''实例化一个 sftp对象,指定连接的通道'''
        sftp = paramiko.SFTPClient.from_transport(trans)
        '''发送文件'''
        print (local_file+"    "+remote_path)
        if os.path.exists(local_file):
            sftp.put(localpath=local_file, remotepath=remote_path)
        else:
            raise "sites.tar.gz不存在"
        '''下载文件'''
        # sftp.get(remotepath, localpath)
        trans.close()

class Build(object):
    """
    code_path 代码存储路径
    profile 编译配置
    webents 执行编译的webent list
    """
    def __init__(self, code_path, profile,webents):
        self.code_path = code_path
        self.profile = profile
        self.webents = webents
    '''编译函数'''
    def mvn(self):
        for webent in self.webents:
            webent_path = self.code_path + os.path.sep + webent
            if os.path.exists(webent_path):
                os.chdir(webent_path)
                try:
                    print("编译" + webent)
                    subprocess.check_call(['mvn','-q','-ff','clean','install','-P',self.profile],shell=True)
                    print("编译完成！")
                except subprocess.CalledProcessError:
                    print("编译错误！请修正代码重新编译！")
            else:
                print(webent_path + "路径不存在，请确认是否有该项目名")

    '''打包函数，将所有编译的包移动到统一目录，默认为账户根目录下的sites'''
    def tar_targets(self):
        """设定user主目录"""
        usr_home_path = os.path.expanduser('~')
        sites_path = usr_home_path+os.path.sep+"sites"
        '''删除原来的目录存档，再新建'''
        if os.path.exists(sites_path):
            rmtree(sites_path)
        os.mkdir(sites_path)
        for site in self.webents:
            site_name =self.get_site_name(site)
            target_path = sites_path + os.path.sep + site_name + os.path.sep
            ROOT_war_path = self.code_path + os.path.sep + site + os.path.sep + 'target' + os.path.sep + 'ROOT.war'
            RPC_jar_path = self.code_path + os.path.sep + site + os.path.sep + 'target' + os.path.sep + site +'.jar'
            RPC_lib_path = self.code_path + os.path.sep + site + os.path.sep + 'target' + os.path.sep + 'lib'
            '''wm-msger的静态资源单独配置'''
            Msger_resource_path=self.code_path + os.path.sep + site + os.path.sep + 'target' + os.path.sep + 'resources'
            if os.path.exists(ROOT_war_path):
                os.mkdir(target_path)
                copy2(ROOT_war_path,target_path)
            if os.path.exists(RPC_jar_path):
                copytree(RPC_lib_path, target_path + os.path.sep + 'lib')
                copy2(RPC_jar_path, target_path)
                if os.path.exists(Msger_resource_path):
                    copytree(Msger_resource_path, target_path + os.path.sep + 'resources')
        '''打包'''
        make_archive("sites", 'gztar', root_dir=sites_path, base_dir=None, verbose=0,
                     dry_run=0, owner=None, group=None, logger=None)

        '''移动到登录账户目录'''
        if os.path.exists("sites.tar.gz"):
            if os.path.exists(os.path.expanduser('~')+os.path.sep+"sites.tar.gz"):
                os.remove(os.path.expanduser('~')+os.path.sep+"sites.tar.gz")
            move("sites.tar.gz",os.path.expanduser('~'))
    '''取得webent发布的名称'''
    def get_site_name(self,site):
        if  site.find('webent') != -1:
            site_name = site[(site.index('-') + 1):site.rindex('-')]
        else:
            site_name = site[(site.index('-') + 1):]

        return site_name

class Git_config(object):
    """
    code_path 代码存储路径
    branch 分支
    """

    def __init__(self,code_path,branch):
        self.code_path = code_path
        self.branch = branch

    def pull(self):
        os.chdir(self.code_path)
        try:
            subprocess.check_call(['git', 'checkout', self.branch], shell=True)
            subprocess.check_call(['git', 'pull','origin', self.branch], shell=True)
        except subprocess.CalledProcessError:
            print ("ERROR")

# git=Git_config("D:\Code\ArhasMK",'develop')
# git.pull()
build=Build("D:\Code\ArhasMK",'st-https',['mk-aggregator','mk-wm-webent','mk-lake-webent','mk-imgr-webent','mk-lake-imgr-webent'])
# build.mvn()
build.tar_targets()
#server=Server('175.155.75.217','admin',5555)
#server.sftp('Yam2017#')
#server.ssh()

