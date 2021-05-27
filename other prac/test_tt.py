from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()

url = "http://www.testingedu.com.cn:8000/Home/user/login.html"
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_id("username").send_keys("13800138006")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("verify_code").send_keys("1")
driver.find_element_by_css_selector(".J-login-submit").click()
# driver.find_element_by_partial_link_text("返回商城首页").click()
driver.find_element_by_partial_link_text("我的订单").click()

sleep(5)
# driver.find_element_by_partial_link_text("我的收藏").click()

eles = driver.find_elements_by_css_selector(".menumain>#navitems5 a")
print(eles)

# driver.find_element_by_xpath("//div/div[@id='navitems5']/ul/li[2]").click()

# 点击立即支付
driver.find_element_by_xpath("//a[@class='ps_lj' and @target='_blank'][1]").click()
# driver.find_element_by_xpath("//table[2]/tbody/tr//td/div/div/a[@class='ps_lj']").click()
sleep(3)

# 选择付款方式
driver.find_element_by_css_selector("input[value='pay_code=cod']").click()
# 是否提交成功
suc_text = driver.find_element_by_xpath("//div[@class='erhuh']/h3")
print(suc_text.text)

sleep(3)
driver.quit()
