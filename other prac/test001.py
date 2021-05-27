from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://hy.smartont.net:8440/#/login")

driver.find_element_by_css_selector(".input[type='text']").send_keys("18000000202")
sleep(2)
driver.find_element_by_css_selector(".input[type='password']").send_keys("Abc1234@")
sleep(2)
driver.find_element_by_css_selector(".u_btn_big").click()

driver.quit()
