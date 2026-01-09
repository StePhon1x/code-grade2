"""
字符串
"""

# 1. 查找操作
text = "Python是一门强大的编程语言"
print(text.find("强大"))  # 返回索引
print(text.rfind("强大"))  # 返回索引，从右侧开始查找
print(text.index("编程"))  # 类似find，但找不到会报错
print(text.rindex("编程"))  # 类似rfind，但找不到会报错
print(text.count("P"))  # 计数出现次数
print(text.startswith("Py"))  # 开头判断
print(text.endswith("言"))  # 结尾判断

# 2. 验证操作
num_str = "12345"
print(num_str.isdigit())  # 是否全数字
print("abc".isalpha())  # 是否全字母
print("abc123".isalnum())  # 是否字母或数字
print("  ".isspace())  # 是否全空白字符
print("Python".isupper())  # 是否全大写
print("python".islower())  # 是否全小写

# 3. 分割与连接
csv_data = "apple,banana,orange,grape"
fruits = csv_data.split(",")  # 分割
print("|".join(fruits))  # 连接

url = "https://www.example.com/path"
head, sep, tail = url.partition("://")  # 分割为三部分
head, sep, tail = url.rpartition("/")  # 从右侧分割为三部分


# 4. 转换操作
text = "Python Programming"
print(text.upper())  # 转大写
print(text.lower())  # 转小写
print(text.capitalize())  # 首字母大写
print(text.title())  # 每个单词首字母大写
print(text.swapcase())  # 大小写互换

# 5. 清洗操作
dirty_text = "  Python编程  "
print(dirty_text.replace("编程", "语言"))  # 替换子串
print(dirty_text.strip())  # 去除两端空白
print(dirty_text.lstrip())  # 去除左端空白
print(dirty_text.rstrip())  # 去除右端空白

maketrans_table = str.maketrans("aeiou", "12345")
cleaned_text = dirty_text.translate(maketrans_table)  # 字符替换
print(cleaned_text)

# 6. 格式化与排版
name = "小明"
age = 20
# 三种格式化方式
print("姓名:%s, 年龄:%d" % (name, age))  # %格式化
print("姓名:{}, 年龄:{}".format(name, age))  # format方法
print(f"姓名:{name}, 年龄:{age}")  # f-string

# 排版
text = "Python"
print(text.ljust(10, "*"))  # 左对齐
print(text.rjust(10, "*"))  # 右对齐
print(text.center(10, "*"))  # 居中对齐

# 7. 表达式求值
evaluate_expression = "3 + 5 * 2"
result = eval(evaluate_expression)
print(f"表达式 {evaluate_expression} 的结果是: {result}")


"""
正则表达式
"""

import re

# 1. 基本匹配
text = "我的电话是123-4567-8901，另一个是987-6543-2100"
pattern = r"\d{3}-\d{4}-\d{4}"  # 匹配电话号码
matches = re.findall(pattern, text)
print("找到的电话号码:", matches)

# 2. 常用元字符
# . 匹配任意字符（除了换行符）
# \d 匹配数字
# \w 匹配字母、数字、下划线
# \s 匹配空白字符
# ^ 匹配开头
# $ 匹配结尾
# * 匹配0次或多次
# + 匹配1次或多次
# ? 匹配0次或1次
# {n} 匹配n次
# {n,} 匹配至少n次
# {n,m} 匹配n到m次

# 3. 字符集
pattern = r"[A-Za-z]+"  # 匹配一个或多个字母
text = "Python3.9 发布了"
print(re.findall(pattern, text))

# 4. 分组与捕获
text = "2023-12-25"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
match = re.search(pattern, text)
if match:
    print("完整匹配:", match.group(0))
    print("年:", match.group(1))
    print("月:", match.group(2))
    print("日:", match.group(3))

# 5. 替换操作
text = "价格是$99.99和$149.99"
new_text = re.sub(r"\$\d+\.\d+", "[价格]", text)
print("替换后:", new_text)

# 6. 分割操作
text = "apple, banana; orange. grape"
items = re.split(r"[ ,;.]+", text)
print("分割结果:", items)

"""
函数
"""


# 1. 形参与实参
def greet(name):  # name是形参
    return f"Hello, {name}!"


print(greet("Alice"))  # "Alice"是实参


# 2. 普通位置参数
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")


describe_pet("dog", "Buddy")  # 必须按顺序传递


# 3. 默认值参数
def describe_pet2(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")


describe_pet2("Buddy")  # 使用默认值
describe_pet2("Whiskers", "cat")  # 覆盖默认值


# 4. 关键参数（关键字参数）
def describe_pet3(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")


describe_pet3(pet_name="Buddy", animal_type="dog")  # 关键字参数，顺序不重要


# 5. 可变长度参数
# *args: 接收任意数量的位置参数，打包为元组
def make_pizza(*toppings):
    print("Making pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("mushrooms", "pepperoni", "cheese")


# **kwargs: 接收任意数量的关键字参数，打包为字典
def build_profile(first, last, **user_info):
    profile = {"first_name": first, "last_name": last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("John", "Doe", age=30, location="NYC")
print(user_profile)


# 6. 参数序列解包
def print_coordinates(x, y, z):
    print(f"坐标: ({x}, {y}, {z})")


# 使用*解包序列
coordinates = (10, 20, 30)
print_coordinates(*coordinates)  # 等价于 print_coordinates(10, 20, 30)

# 使用**解包字典
params = {"x": 1, "y": 2, "z": 3}
print_coordinates(**params)  # 等价于 print_coordinates(x=1, y=2, z=3)

# 7.lambda表达式


# 传统函数
def square(x):
    return x**2


# lambda表达式
square_lambda = lambda x: x**2

print(square(5))
print(square_lambda(5))

# map函数结合lambda
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# filter函数结合lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# sorted函数结合lambda
words = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length)  # ['date', 'apple', 'banana', 'cherry', 'elderberry']

# min与max结合lambda使用
words = ["apple", "banana", "cherry", "date", "elderberry"]
shortest = min(words, key=lambda x: len(x))
longest = max(words, key=lambda x: len(x))
print(f"最短: {shortest}, 最长: {longest}")  # 最短: date, 最长: elderberry


# lambda作为高阶函数的参数
def add(a, b):
    return a + b


def operate_on_numbers(a, b, operation):
    return operation(a, b)


result1 = operate_on_numbers(10, 5, add)
print(result1)
result2 = operate_on_numbers(10, 5, lambda x, y: x + y)
print(result2)
