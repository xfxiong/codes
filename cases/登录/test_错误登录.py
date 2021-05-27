import pytest
from selenium import webdriver
import time


class Test_login:

    def test_UI0001(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('http://127.0.0.1/mgr/sign.html')
        # driver.find_element_by_id('username').send_keys()
        driver.find_element_by_id('password').send_keys('88888888')
        driver.find_element_by_tag_name('button').click()
        time.sleep(2)
        alertText = driver.switch_to.alert.text
        print(alertText)
        assert alertText == '请输入用户名'

    def test_UI0002(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('http://127.0.0.1/mgr/sign.html')
        driver.find_element_by_id('username').send_keys('byhy')
        # driver.find_element_by_id('password').send_keys('88888888')
        driver.find_element_by_tag_name('button').click()
        time.sleep(2)
        alertText = driver.switch_to.alert.text
        print(alertText)
        assert alertText == '请输入密码'
