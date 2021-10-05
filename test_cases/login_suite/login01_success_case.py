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
    def test01_loginsuccess(self):
        '''case01 使用test01 newdream123 测试能否登录'''
        log.login(self.driver,'test01','newdream123')
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="user-name"]'), '测试人员1')))  # 断言

    def test02_loginsuccess(self):
        '''case02 使用test02 newdream123 测试能否登录'''
        log.login(self.driver, 'test02', 'newdream123')
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="user-name"]'), '测试人员2')))  # 断言

if __name__=='__main__':
    unittest.main()