import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}


# 如果https是不受信任的证书发起请求的,那么将怕娶不到
# 解决方法 :在requests.get 或者 requests.post方法中 加入verify=False
req = requests.get(url='https://inv-veri.chinatax.gov.cn/', headers=headers, verify=False)

req.encoding = 'utf-8'

# text编码格式是按照默认的解析器的编码来解析的,有可能会出现乱码
# 解决乱码的方法,先通过查看原网站的源代码中设置的编码格式
# 然后把encoding设置为相同的编码格式
print(req.text)
