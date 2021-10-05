import os
import time
import unittest
import HTMLTestRunner

current_path=os.path.dirname(__file__)
now_time = time.strftime('%Y_%m_%d_%H_%M_%S')  # 获取当前时间
report_path = os.path.join(current_path, 'report/resuite%s.html'%now_time)

cases_path=os.path.join(current_path, 'test_cases')#测试用例路径


discover=unittest.defaultTestLoader.discover(start_dir=cases_path,
                                             pattern='*_case.py',
                                             top_level_dir=cases_path)
main_suite=unittest.TestSuite()
main_suite.addTest(discover)

# 指定报告创建的地址及文件名，为了下次生成的报告不覆盖上次的报告，文件名配置了
# 生成报告的当前时间%now_time

file = open(report_path, 'wb')
html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                            title='禅道UI自动化测试项目',
                                            description='由自动化测试组完成，包含大部分功能的自动化')
#注意：用run()方式时使用main(),否则无法生成测试报告
html_runner.run(main_suite)
