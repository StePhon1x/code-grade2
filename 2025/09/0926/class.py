# 创建
dict_x = {}
dict_x = dict()
a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}

# 类型转换
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3, 4]
# dictionary = dict(zip(keys, values))
# print(dictionary)
# d = dict(name = 'Dong', age = 37)
# print(d)

# 访问
aDict = {'name' : 'Dong', 'sex' : 'male', 'age' : 37}
for key in aDict:
    print(key)
print(aDict.keys())
print(aDict.values())
for key, value in aDict.items():
    print(key, value)
#添加 key-value
aDict['age'] = 38
aDict['tel'] = '123456789'
print(aDict)
# 区别
aDict['weight'] = aDict['weight']+1
aDict['weight'] = aDict.get('weight', 100)+1
#字典更新字典
aDict.update({'a':'a', 'b':'b', 'age':43})
print(aDict)















