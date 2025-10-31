# 示例1：无参数函数
def greet():
    """问候函数"""
    print("Hello, Python!")

# 示例2：带参数函数
def greet_person(name):
    """向指定人问候"""
    print(f"Hello, {name}!")

# 示例3：带返回值函数
def add_numbers(a, b):
    """计算两数之和"""
    result = a + b
    return result

# 函数调用
greet()
greet_person("张三")
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")




















'''
形参与实参
'''

# 形参：name, age
def introduce(name, age):
    print(f"我叫{name}，今年{age}岁")

# 实参："李四", 20
introduce("李四", 20)

















'''
参数类型
'''

# 1 普通位置参数 （positional arguments）
# 调用函数时实参和形参的顺序必须严格一致，并且实参和形参的数量必须相同
def power(base, exponent):
    return base ** exponent
print(power(5, 2))   



# 2 默认值参数
# 默认值参数必须出现在函数参数列表的最右端，任何一个默认值参数右边不能有非默认值参数
def power(base, exponent=2):
    return base ** exponent
print(power(5))      # 输出: 25
print(power(5, 3))   # 输出: 1


# 3 关键参数
# 实参顺序可以和形参顺序不一致，但不影响传递结果
# 目的：避免了用户需要牢记位置参数顺序的麻烦
def power(base, exponent=2):
    return base ** exponent
print(power(exponent=3, base=5))  # 输出: 125














# 4 可变长度参数
'''
 *args：接收任意数量的位置参数(列表、元组、集合)，函数内部将其视为一个元组
 [,,,,] (,,,,) {,,,,,}
 **kwargs：接收任意数量的关键字参数（字典），函数内部将其视为一个字典
 '''
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all(1, 2, 3, 4, 5))  # 输出: 15
print(sum_all(10, 20))         # 输出: 30

def sum_all(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value
    return total
print(sum_all(a=10, b=20, c=30))  # 输出: 60












# 5 参数序列解包


def introduce(name, age, city):
    print(f"{name}，{age}岁，来自{city}")

# 传统方式
introduce("张三", 20, "北京")

# 序列解包
info = ["李四", 22, "上海"]
introduce(*info)  # 等价于 introduce("李四", 22, "上海")

# 字典解包
info_dict = {"name": "王五", "age": 25, "city": "广州"}
introduce(**info_dict)












'''
return语句
'''
# 单值返回
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

result = check_even(4)
print(result)  # True

# 多值返回
def calculate_statistics(numbers):
    """计算统计信息"""
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, count, average, maximum, minimum

total, count, avg, max_val, min_val = calculate_statistics([1, 2, 3, 4, 5])

# 提前返回
def login(username, password):
    """登录验证"""
    if not username:
        return False, "用户名不能为空"
    
    if not password:
        return False, "密码不能为空"
    
    # 模拟验证逻辑
    if username == "admin" and password == "123456":
        return True, "登录成功"
    else:
        return False, "用户名或密码错误"













'''
变量作用域
'''
global_var = "我是全局变量"

def test_scope():
    local_var = "我是局部变量"
    print(f"函数内访问全局变量：{global_var}")
    print(f"函数内访问局部变量：{local_var}")

test_scope()
print(f"函数外访问全局变量：{global_var}")
# print(f"函数外访问局部变量：{local_var}")  # 错误！


# 使用global关键字修改全局变量
count = 0

def increment():
    global count  # 声明使用全局变量
    count += 1
    print(f"当前计数：{count}")

increment()
increment()
print(f"最终计数：{count}")















'''
lambda表达式
lambda表达式可以用来声明匿名函数，也就是没有函数名字的临时使用的小函数
适合需要一个函数作为另一个函数参数的场合。
lambda表达式只可以包含一个表达式，该表达式可以任意复杂，其计算结果可以看作是函数的返回值。
'''

# 传统函数
def square(x):
    return x ** 2

# lambda表达式
square_lambda = lambda x: x ** 2

print(square(5))          
print(square_lambda(5))   


'''
map与lambda结合使用，可以对一个可迭代对象的每个元素应用一个函数，并返回一个新的可迭代对象。
map(function, iterable, ...)
  function：要应用的函数
  iterable：一个或多个可迭代对象（列表、元组、字符串等）
  返回值：一个map对象（迭代器）
'''
numbers = [1, 2, 3, 4, 5]

# Before:定义独立的平方函数
def square(x):
    return x ** 2

squares = list(map(square, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# After:使用lambda表达式
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]




'''
filter与lambda结合使用，可以过滤一个可迭代对象的元素，返回符合条件的元素组成的新可迭代对象。
filter(function, iterable)
    function：判断函数，返回True或False
    iterable：可迭代对象（列表、元组、字符串等）
    返回值：一个filter对象（迭代器），包含使function返回True的元素
'''
numbers = [1, 2, 3, 4, 5]
# Before:定义独立的偶数过滤函数
def is_even(x):
    return x % 2 == 0
evens = list(filter(is_even, numbers))
print(evens)  # [2, 4]

# After:使用lambda表达式
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)    # [2, 4]














'''
sorted与lambda结合使用，可以根据自定义的排序规则对一个可迭代对象进行排序。
sorted(iterable, key=None, reverse=False)
    iterable：可迭代对象（列表、元组、字符串、字典等）
    key：排序的关键函数（可选）
    reverse：是否反向排序，默认为False（升序）
    返回值：一个新的排序后的列表
'''
words = ["apple", "banana", "cherry", "date", "elderberry"]
# 按照单词长度排序
sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length)  # ['date', 'apple', 'banana', 'cherry', 'elderberry']

'''
min与max结合lambda使用，可以根据自定义的规则找出最小值或最大值。
min(iterable, key=None, default=None)
max(iterable, key=None, default=None)
    iterable：可迭代对象（列表、元组、字符串、字典等）
    key：用于比较的关键函数（可选）
    default：如果iterable为空时返回的默认值（可选）
    返回值：最小值或最大值
'''

# 按字符串长度找最短/最长
words = ["apple", "banana", "cherry", "date", "elderberry"]
shortest = min(words, key=lambda x: len(x))
longest = max(words, key=lambda x: len(x))
print(f"最短: {shortest}, 最长: {longest}")  # 最短: date, 最长: elderberry


'''
lambda作为高阶函数的参数
'''
#   map(function, iterable, ...)
def add(a, b):
    return a + b

def operate_on_numbers(a, b, operation):
    return operation(a, b)

result1 = operate_on_numbers(10, 5, add)
print(result1)
result2 = operate_on_numbers(10, 5, lambda x, y: x + y)
print(result2)  
