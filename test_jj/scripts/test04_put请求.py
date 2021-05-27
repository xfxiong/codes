"""
    目标：put方法
    案例:
    参数：
        1.json :传入json字符串
        2.headers :传入请求信息头信息
    响应：
        1.响应对象.json()
"""
import requests

url = "http://127.0.0.1:8000/api/departments/TT702/"

# headers
headers = {"Content-Type": "application/json"}

# json
data = {
    "data": [{
        "dep_id": "TT702",
        "dep_name": "TestTT702update学",
        "master_name": "Test-Master",
        "slogan": "Here is Slogan"
    }]
}

resp = requests.put(url, json=data, headers=headers)

print(resp.status_code)
print(resp.json())
