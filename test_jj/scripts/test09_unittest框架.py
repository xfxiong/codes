"""
	目标：unittest框架中完成 登录Tpshop查询我的订单
	案例数据：
		1.获取验证码：http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=verify
		2.登录接口：http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login
		3.订单：http://www.testingedu.com.cn:8000/Home/Order/order_list.html
		4.登录数据
			data ={"username": "13800138006",
					"password": "123456",
					"verify_code": 1}
"""
# 导包 unittest request
import unittest
import requests


# 新建测试类
class TestLogin(unittest.TestCase):
    # setup
    def setUp(self) -> None:
        pass

    # teardown
    def tearDown(self) -> None:
        pass

    # 登录成功
    def test_login_success(self):
        pass

    # 账号不存在
    def test_username_not_exist(self):
        pass

    # 密码错误
    def test_password_error(self):
        pass
