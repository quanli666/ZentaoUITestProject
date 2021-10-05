import os
import configparser

current_path=os.path.dirname(__file__)
conf=os.path.join(current_path,'local_config.ini')
class Config_info:
    def __init__(self,conf_path=conf):
        '''
        该构造方法用于封装configparser访问配置文件.ini
        :param config_path:
        '''
        self.__conf_path=conf_path#使用配置文件所在的地址
        self.__conf=configparser.ConfigParser()#使用ConfigParser初始化对象,首选需要初始化实例
        self.__conf.read(self.__conf_path,encoding='utf-8')#读取配置文件
    def read_ini(self,section,option):
        value=self.__conf.get(section,option)#获取.ini文件中section下的option的值
        return value
    @property
    def get_read_url(self):
        value=self.read_ini('default','URL')#获取配置文件信息
        return value
Config=Config_info()
if __name__=='__main__':
    config = Config_info()
    print(config.get_read_url)
