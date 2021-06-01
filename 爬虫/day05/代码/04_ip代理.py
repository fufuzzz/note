import requests

# print(req.text)

# 设置代理ip
# proxy = {
#
#     '请求的方式(http/https)': 'ip端口'
# }

proxy = {

    'http': '175.44.108.107:9999'
}
req = requests.get(url='http://httpbin.org/ip', proxies=proxy)