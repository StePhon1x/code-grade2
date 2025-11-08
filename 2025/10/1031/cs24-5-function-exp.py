'''
习题一：同一功能的三种函数形式
编写三个函数，都实现计算矩形面积&输出（print）的功能：
    area_no_params() - 无参数函数，从用户输入获取长和宽
    area_with_params(length, width) - 带参数函数
    area_with_return(length, width) - 带返回值函数
'''

# 1. 无参数函数
def area_no_params():
    """从用户输入获取长和宽并计算面积并输出"""

    length = int(input("输入长："))
    width = int(input("输入宽："))
    
    result = length*width
    print(f"矩形面积: {result}")



# 2. 带参数函数
def area_with_params(length, width):
    """接收参数并计算面积,输出结果"""

    result = length*width
    print(f"矩形面积: {result}")
    

# 3. 带返回值函数
def area_with_return(length, width):
    """计算面积并返回结果"""

    return length*width
    

# 测试代码
print("=== 无参数函数 ===")
area_no_params()

print("\n=== 带参数函数 ===")
area_with_params(5, 3)

print("\n=== 带返回值函数 ===")
result = area_with_return(5, 3)
print(f"矩形面积: {result}")


'''
习题二：lambda表达式练习
'''

students = [
    {"name": "Alice", "age": 20, "score": 85, "major": "计算机"},
    {"name": "Bob", "age": 22, "score": 92, "major": "数学"},
    {"name": "Charlie", "age": 19, "score": 78, "major": "物理"},
    {"name": "Diana", "age": 21, "score": 88, "major": "计算机"},
    {"name": "Eve", "age": 23, "score": 95, "major": "数学"}
]

print("=== 1. lambda与map结合 ===")
# 将学生姓名转换为大写，返回姓名列表upper_names
# 在此处写代码

upper_names = list(map(lambda s: s["name"].upper(), students))

print(f"大写姓名: {upper_names}")


print("\n=== 2. lambda与filter结合 ===")
# 过滤计算机专业的学生
# 在此处写代码

cs_students = list(filter(lambda s: s["major"] == "计算机", students))

print(f"计算机专业学生: {[s['name'] for s in cs_students]}")


print("\n=== 3. lambda与sorted结合 ===")
# 按年龄排序，在此处写代码

by_age = list(sorted(students, key = lambda s: s["age"]))

print("按年龄排序:")
for student in by_age:
    print(f"{student['name']}: {student['age']}岁")


print("\n=== 4. lambda与min结合 ===")
# 找年龄最小的学生，在此处写代码

youngest = min(students, key = lambda s: s["age"])

print(f"年龄最小的学生: {youngest['name']} ({youngest['age']}岁)")


print("\n=== 5. lambda作为高阶函数的参数 ===")
def process_data(data, processor):
    """高阶函数：对数据进行处理"""
    return processor(data)
# 使用lambda作为处理函数，在此处写代码：筛选出分数大于85的学生姓名列表
result = process_data(students, lambda l: [s["name"] for s in l if s["score"] > 85])
print(f"高分学生: {result}")