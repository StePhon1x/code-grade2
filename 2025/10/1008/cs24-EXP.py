'''
给定数据：计算机班级的学生信息（有重复记录）
# 任务1： 观察原始数据，有什么问题？
'''
raw_students = [
    '张三-男-90', '李四-女-85', '王五-男-88', 
    '赵六-女-92', '张三-男-90', '钱七-男-87'
]
# 问题：数据重复'张三-男-90' 出现了两次，属于重复记录。
# 成绩是字符串 "90"、"85" 等，应转换为 整数或浮点数 才能进行计算

'''
任务2：数据清洗与转换
将每个字符串转换为元组格式[（'张三', '男', '90'）,...],
# 切分字符串用split('-')
'''
students_tuples = []

# 学生在此处编写代码
for item in raw_students:
    parts = item.split('-')
    students_tuples.append(tuple(parts))

print("\n转换后的元组列表：")
print(students_tuples)

'''
任务3：数据去重与分析
# 使用集合去除重复记录,将去重后的数据转换回列表 clean_students
'''
# 学生在此处编写代码
temporary_set = set(students_tuples)
clean_students = list(temporary_set)

print(f"\n去重前：{len(students_tuples)} 条记录")
print(f"去重后：{len(clean_students)} 条记录")

'''
任务4：构建结构化数据
创建字典，以姓名为键，完整信息为值 {'张三':{'name':'张三' , 'gender': '男', 'score': 90} , ...}
'''

students_dict = {}

# 学生在此处编写代码
for name, gender, score in clean_students:
    students_dict[name] = { 
        "name": name,
        "gender": gender,
        "score": int(score)
    }

print("\n学生信息字典：")
for name, info in students_dict.items():
    print(f"{name}: {info}")


'''
任务5：数据统计
5.1 统计男生和女生人数
'''

gender_count = {'男': 0, '女': 0}

# 学生在此处编写代码
for info in students_dict.values():
    gender = info["gender"]
    if gender in gender_count:
        gender_count[gender] += 1

print(f"\n性别统计：{gender_count}")

'''
5.2 计算班级平均成绩 average_score
'''
total_score = 0

# 学生在此处编写代码
for info in students_dict.values():
    total_score += info["score"]
average_score = total_score/len(students_dict)

print(f"班级平均分：{average_score:.2f}")