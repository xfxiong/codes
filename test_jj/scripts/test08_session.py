"""
	目标：通过session对象 登录Tpshop查询我的订单
	案例数据：
		1.获取验证码：http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=verify
		2.登录接口：http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login
		3.订单：http://www.testingedu.com.cn:8000/Home/Order/order_list.html
		4.登录数据
			data ={"username": "13800138006",
					"password": "123456",
					"verify_code": 1}
"""
import requests

# 获取session对象
session = requests.session()

# 请求验证码记录cookies
url_verify_code = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=verify"
session.get(url_verify_code)

# 请求登录
url_login = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login"
data = {"username": "13800138006",
        "password": "123456",
        "verify_code": 1}

resp = session.post(url=url_login, data=data)

# 验证是否登录成功
print(resp.json())

# 查询订单
url_order = "http://www.testingedu.com.cn:8000/Home/Order/order_list.html"
resp = session.get(url=url_order)
print(resp.text)
