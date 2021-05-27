"""
    目标：delete方法
    案例:删除

    响应：
        1.响应状态码
"""
import json

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

resp = requests.put(url, json=json.dumps(data), headers=headers)

print(resp.status_code)
print(resp.json())
