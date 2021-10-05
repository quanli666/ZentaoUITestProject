import os
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.login import log
from common.set_driver import setDri

current_path=os.path.dirname(__file__)
chrome_path=os.path.join(current_path,'../../webdriver/chromedriver.exe')

class Main01LinkCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=setDri.set_driver
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
    def test_loginfail(self):
        '''case03 使用test01 newdream12 测试能否登录成功'''
        log.login(self.driver,'test01','newdream12')
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.alert_is_present()))

if __name__=='__main__':
    unittest.main()