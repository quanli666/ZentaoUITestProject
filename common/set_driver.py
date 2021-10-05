import os
from selenium import webdriver
from conf.confing import Config
current_path=os.path.dirname(__file__)
chrome_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
class SetDriver:
    @property
    def set_driver(self):  # 把selenium的初始化配置放入
        self.driver = webdriver.Chrome(executable_path=chrome_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(Config.get_read_url)  # 导入了配置文件中的地址
        return self.driver
setDri=SetDriver()
if __name__=='__main__':
    SD=SetDriver()
    SD.set_driver