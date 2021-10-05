import os
import time
import unittest
from selenium.webdriver.common.by import By
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
        self.driver.find_element(By.XPATH,'//span[@class="user-name"]').click()
        self.driver.find_element(By.XPATH,'//a[contains(@href,"php?m=user&f=logout")]').click()
        time.sleep(2)
        self.driver.quit()
    def test_my_link(self):
        '''case04 验证我的地盘菜单能否正确链接'''
        log.login(self.driver,'test01','newdream123')
        self.driver.find_element(By.XPATH,'//li[@data-id="my"]').click()
        self.assertTrue(WebDriverWait(self.driver,6).until(EC.title_is('我的地盘 - 禅道')))

    def test_product_link(self):
        '''case05 验证产品主页菜单能否正确链接'''
        log.login(self.driver,'test01','newdream123')
        self.driver.find_element(By.XPATH,'//li[@data-id="product"]').click()
        self.assertTrue(WebDriverWait(self.driver,6).until(EC.title_is('产品主页 - 禅道')))

if __name__=='__main__':
    unittest.main()