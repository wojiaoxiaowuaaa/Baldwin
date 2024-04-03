import json

d = {'result': '{"detailes": "success", "isSuccess": true}'}

print(type(d['result']))
print(d['result'])

fell = json.loads(d['result'])
print(fell)
print(type(fell))

"""<class 'str'>
{"detailes": "success", "isSuccess": true}
{'detailes': 'success', 'isSuccess': True}
<class 'dict'>"""

# 如果使用eval() 函数强转的话会报错NameError: name 'true' is not defined因为Python中的True首字母必须是大写的与json不同
# json.load方法可以自动将json字符串中的小写的true转换为Python中的True
