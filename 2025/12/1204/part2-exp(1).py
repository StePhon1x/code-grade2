"""
题目一：字符串操作练习
1. 接收用户输入的邮箱地址
2. 验证邮箱是否合法（必须包含@和.，且@在.之前）
3. 提取邮箱的用户名和域名部分
4. 输出验证结果和提取的信息

"""

# import re
# def validate_and_extract_email(email):
#     # 此处编写代码
#     email_pattern = r'^[^@]+@[^@]+\.[^@]+$'
#     if re.fullmatch(email_pattern, email):
#         username, domain = email.split("@", 1)
#         print(True, username, domain)
#     else:
#         print(False, None, None)

# # 测试代码
# validate_and_extract_email("user@example.com")
# validate_and_extract_email("userexample.com")
# validate_and_extract_email("user@examplecom")

"""
题目二：文本清洗与格式化
任务：
1. 去除文本两端的空白字符
2. 将文本中所有英文单词转为小写
3. 统计文本中逗号的数量
4. 将文本按逗号分割成多个部分

"""
# raw_text = "   Python 是一种解释型、高级编程语言,由Guido van Rossum于1991年发布。  "
# #1. 去除文本两端的空白字符
# raw_text = raw_text.strip()
# #2. 将文本中所有英文单词转为小写
# raw_text = raw_text.lower()
# #3. 统计文本中逗号的数量
# Count = raw_text.count(",")
# #4. 将文本按逗号分割成多个部分
# raw_text_split = raw_text.split(",")
# print(raw_text_split)

"""
题目三:提取邮箱地址 （使用正则表达式）
从一段简单的文本中提取所有格式正确的邮箱地址。
要求
1.提取所有格式正确的邮箱地址
2.邮箱格式要求：用户名@域名.后缀
3.用户名可以包含字母、数字、点号、下划线
4.后缀至少2个字母
"""

# import re
# text = """
# 我的邮箱是：abc@test.com
# 同事邮箱：xyz@company.cn
# 客服邮箱：service@example.org
# 无效邮箱：test@, @example.com, user@
# """

# # 在此处编写正则表达式模板email_pattern
# email_pattern = r'\w+@\w+\.\w{2,}'
# emails = re.findall(email_pattern, text)
# for email in emails:
#     print(f"找到的邮箱地址: {email}")


"""
题目四：学生信息处理函数
设计一个学生信息处理函数，要求：
1. 必需参数：姓名、学号
2. 默认参数：班级（默认"计算机1班"）
3. 可变位置参数：接受多门课程成绩
4. 可变关键字参数：接受其他任意信息
5. 函数返回学生的完整信息字典
"""


# 在此处设计函数student_info
def student_info(name, id, class_name="计算机1班", *rest_args, **kwargs):
    class_name_last = class_name
    grades = []
    if isinstance(class_name_last, str):
        grades = rest_args
    else:
        class_name_last = "计算机1班"
        grades = (class_name,) + rest_args
    return {
        "name": name,
        "id": id,
        "class": class_name_last,
        "grades": grades,
        **kwargs,
    }


# 测试用例
info1 = student_info("张三", "2023001", 85, 90, 78, age=20, gender="男")
info2 = student_info("李四", "2023002", "软件2班", 92, 88, 95, hobby="篮球")
info3 = student_info("王五", "2023003", 75, 80, 85, 90, email="wang@example.com")

# 打印结果
print("学生1:", info1)
print("学生2:", info2)
print("学生3:", info3)
