
# 加密
#  base64编码
#  md5加密: 不可逆的加密算法, 明文和密文是一一对应的
#       加密: 明文 => 密文
#       解密: 密文 => 明文
#  RSA加密: 非对称加密算法, 公钥, 私钥 , 很难解密
#  DES, AES: 对称加密, 需要提供key='abc'
#    在公司会有自己的算法

import hashlib

m = hashlib.md5()
m.update('123456'.encode())
print(m.hexdigest())

print(len('e10adc3949ba59abbe56e057f20f883e'))  # 32

# os模块
# time模块
# datetime模块
