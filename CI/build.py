# -*- coding:utf-8 -*-
import os,random,subprocess
from shutil import copy2,rmtree,copytree,make_archive


class Server(object):
    """
    ip 服务器IP
    user 登录账户，需要前置ssh免密码登录
    port ssh登录的端口
    """
    def __init__(self, ip, user,port):
        self.ip = ip
        self.port = port


class Server_node(Server):
    """
    sites_path 发布的根路径
    webents 服务器上部署的webent list
    """

    def __init__(self, sites_path, webents):
        Server.__init__(self)
        self.sites_path = sites_path
        self.webents = webents

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
            target_path = sites_path + os.path.sep + site
            ROOT_war_path = self.code_path + os.path.sep + site + os.path.sep + 'target' + os.path.sep + 'ROOT.war'
            RPC_jar_path = self.code_path + os.path.sep + site + os.path.sep + 'target' + os.path.sep + site +'.jar'
            RPC_lib_path = self.code_path + os.path.sep + site + os.path.sep + 'target' + os.path.sep + 'lib'
            if os.path.exists(ROOT_war_path):
                copy2(ROOT_war_path,target_path)
            if os.path.exists(RPC_jar_path):
                copytree(RPC_lib_path, target_path)
                copy2(RPC_jar_path, target_path)
        '''打包'''
        make_archive("sites", 'gztar', root_dir=sites_path, base_dir=None, verbose=0,
                     dry_run=0, owner=None, group=None, logger=None)





class Git_config(object):
    """
    code_path 代码存储路径
    branch 分支
    """

bui=Build("D:\Code\ArhasMK","st-https",["mk-wm-webent","mk-imgr-rpc"])
#bui.mvn()
bui.tar_targets()


