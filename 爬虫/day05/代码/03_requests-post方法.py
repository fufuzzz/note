import requests
import json
# 通过字典形式模拟post数据
data = {
    'kw': 'job'
}

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

req = requests.post(url='https://fanyi.baidu.com/sug', data=data, headers=headers)

# print(json.loads(req.text))
print(req.json())