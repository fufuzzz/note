
# json : 是一种数据格式(数据的表示方式)
# xml : 是一种数据格式(数据的表示方式)

# json字符串
# json对象: Python的列表或字典

import json

# json解析/json反序列化: json字符串 => json对象
json_str = '{"name": "zhangsan", "age": 33}'
json_obj = json.loads(json_str)
print(json_obj, type(json_obj))
# {'name': 'zhangsan', 'age': 33} <class 'dict'>

# json序列化: json对象 => json字符串
json_obj2 = {"name": "zhangsan", "age": 33}
json_str2 = json.dumps(json_obj2)
print(json_str2, type(json_str2))
