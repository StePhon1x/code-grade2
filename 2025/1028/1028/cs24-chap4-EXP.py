'''
第一部分：字符串基础操作
题目1：字符串清洗与格式化
    对输入的文本进行清洗和格式化：
    1. 将文本转换为小写
    2. 去除首尾空白字符
    3. 将连续多个空格替换为单个空格
    4. 将"python"替换为"Python"（注意大小写）
    5. 使用format()方法格式化输出："处理结果: [处理后的文本]"

    示例：
    输入: "  Hello   Python  world!  "
    输出: "处理结果: hello Python world!"
'''


import re


def clean_and_format_text(text):
    text = text.replace("  ", " ")
    return "处理结果：{}".format(text.lower().strip().replace("python", "Python").replace("  ", " "))

    # 测试
test_text = "  Hello   Python  world!  "
print(clean_and_format_text(test_text))

'''
题目2：字符串查找与统计
    分析文本并返回统计信息：
    1. 文本总长度
    2. 关键词出现次数（不区分大小写）
    3. 关键词第一次和最后一次出现的位置
    4. 文本中数字字符的数量
    5. 文本是否以字母开头

    返回字典格式：
    {
        'total_length': 总长度,
        'keyword_count': 关键词出现次数,
        'first_position': 第一次位置,
        'last_position': 最后一次位置,
        'digit_count': 数字字符数,
        'starts_with_alpha': 是否以字母开头
    }
'''


def analyze_text(text, keyword):
    # 在此实现
    total_length = len(text)

    # 将文本和关键字都转换为小写
    text_lower = text.lower()
    keyword_lower = keyword.lower()

    # 计算关键字次数
    keyword_count = text_lower.count(keyword_lower)

    # 查找关键字位置
    first_position = text_lower.find(keyword_lower)
    last_position = text_lower.rfind(keyword_lower)

    # 计算数字字符数
    digit_count = 0
    for char in text:
        if char.isdigit():
            digit_count += 1

    # 是否以字母开头
    starts_with_alpha = text[0].isalpha() if text else False

    return {
        'total_length': total_length,
        'keyword_count': keyword_count,
        'first_position': first_position,
        'last_position': last_position,
        'digit_count': digit_count,
        'starts_with_alpha': starts_with_alpha
    }


# 测试
text = "Python3.9 released in 2020, Python3.10 in 2021"
print(analyze_text(text, "python"))


'''
题目3：字符串分割与连接
    处理文件路径字符串：
    1. 按分号分割路径
    2. 对每个路径：
        - 去除首尾空格
        - 将反斜杠替换为正斜杠
        - 提取文件名（最后一个斜杠后的部分）
    3. 用" | "连接所有文件名

    示例：
    输入: "C:\\Users\\test\\file.txt; /home/user/data.csv;  D:\\docs\\report.pdf  "
    输出: "file.txt | data.csv | report.pdf"
'''


def process_file_paths(paths_text):
    # 在此实现
    paths_text = paths_text.split(";")

    path_last = []
    for p in paths_text:
        path_last.append(p.strip().replace("\\", "/").split("/")[-1])

    return " | ".join(path_last)


# 测试
paths = "C:\\Users\\test\\file.txt; /home/user/data.csv;  D:\\docs\\report.pdf  "
print(process_file_paths(paths))

'''
题目4：字符串验证与转换
    验证和转换数据：
    1. 过滤掉空字符串和纯空白字符串
    2. 验证每个字符串：
        - 如果是纯数字，转换为整数
        - 如果是浮点数格式，转换为浮点数
        - 否则保持字符串格式
    3. 统计各种类型的数量

    返回：
    {
        'processed_data': 处理后的数据列表,
        'int_count': 整数数量,
        'float_count': 浮点数数量,
        'str_count': 字符串数量
    }
'''


def validate_and_convert(data_list):
    # 在此实现
    data_list_cleaned = []
    data_list_cleaned = [data for data in data_list if data.strip() != ""]

    str_count = float_count = int_count = 0
    for data in data_list_cleaned:
        try:
            int(data)
            int_count += 1
        except ValueError:
            try:
                float(data)
                float_count += 1
            except ValueError:
                str_count += 1

    return {
        'processed_data': data_list_cleaned,
        'int_count': int_count,
        'float_count': float_count,
        'str_count': str_count
    }


# 测试
data = ["123", "45.67", "hello", "   ", "", "890", "world", "3.14"]
print(validate_and_convert(data))

'''    
第二部分：正则表达式应用
题目5：基础模式匹配
    从文本中提取联系信息：
    1. 提取所有手机号（11位，1开头，第二位3-9）
    2. 提取所有邮箱地址
    3. 提取所有日期（yyyy-mm-dd格式）
    4. 统计每种信息的数量
    
    返回字典格式
'''


def extract_contact_info(text):
    # 在此实现
    pass


# 测试
text = """
联系人：张三，电话13812345678，邮箱zhangsan@test.com，生日1990-05-20
李四：13987654321，lisi@company.cn，注册日期2023-12-15
无效信息：12345，test@，2024-13-45
"""
print(extract_contact_info(text))

'''
题目6：日志分析系统
    分析服务器日志：
    1. 统计每种日志级别（INFO, ERROR, WARN等）的数量
    2. 提取所有IP地址并统计出现次数
    3. 找出所有错误信息（ERROR级别）
    4. 计算日志的时间范围
    返回综合统计信息
'''


def analyze_server_logs(logs_text):
    # 在此实现
    pass


# 测试
logs = """
2024-03-15 10:30:25 INFO User login from 192.168.1.100
2024-03-15 10:35:40 ERROR Database connection failed from 10.0.0.50
2024-03-15 10:40:15 WARN High memory usage from 192.168.1.100  
2024-03-15 10:45:30 INFO File uploaded from 10.0.0.75
2024-03-15 10:50:20 ERROR Permission denied from 192.168.1.200
"""
print(analyze_server_logs(logs))
