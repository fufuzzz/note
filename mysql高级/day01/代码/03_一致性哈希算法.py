import zlib
class Hsahpy:

    def __init__(self):
        # 模拟一个空圆环
        self.node = {}

    # 添加一台服务器, 把服务器对应的ip变成0-2**32的一个随机整形
    def add(self, ip):
        crc32_ip = zlib.crc32(ip.encode())
        self.node[crc32_ip] = ip

    # 把node字典按照key由小到大排序
    @property
    def sort_node(self):
        return dict(sorted(self.node.items()))

    # 寻找数据对应的服务器
    def search_sercer(self, data):
        # 把data进行crc32处理
        crc32_data = zlib.crc32(data.encode())
        print(crc32_data)
        for k, v in self.sort_node.items():
            if k > crc32_data:
                return v

        else:
            return list(self.sort_node.values())[0]



if __name__ == '__main__':
    h = Hsahpy()
    h.add('a')
    h.add('b')
    h.add('c')
    print(h.node)
    # h.sort_node()
    print(h.sort_node)
    print(h.search_sercer('1000'))