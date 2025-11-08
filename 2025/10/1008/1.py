# 原始数据（有重复记录）
raw_students = [
    '张三-男-90', '李四-女-85', '王五-男-88', 
    '赵六-女-92', '张三-男-90', '钱七-男-87'
]

# 任务1：观察数据问题
# 问题：数据重复，成绩是字符串，需要转换为数字

# 任务2：数据清洗与转换
students_tuples = []
for item in raw_students:
    parts = item.split('-')          # 按 '-' 分割
    students_tuples.append(tuple(parts))  # 转换为元组

print("转换后的元组列表：")
print(students_tuples)

# 任务3：去重（保留顺序）
seen = set()
clean_students = []
for s in students_tuples:
    if s not in seen:
        clean_students.append(s)
        seen.add(s)

print(f"\n去重前：{len(students_tuples)} 条记录")
print(f"去重后：{len(clean_students)} 条记录")

# 任务4：构建结构化数据字典
# 使用姓名为键，值为学生信息
students_dict = {}
for name, gender, score in clean_students:
    students_dict[name] = {
        "name": name,
        "gender": gender,
        "score": int(score)
    }

print("\n学生信息字典：")
for name, info in students_dict.items():
    print(f"{name}: {info}")

# 任务5.1：统计男生和女生人数
gender_count = {'男': 0, '女': 0}
for info in students_dict.values():
    gender = info["gender"]
    if gender in gender_count:
        gender_count[gender] += 1

print(f"\n性别统计：{gender_count}")

# 任务5.2：计算班级平均成绩
total_score = 0
for info in students_dict.values():
    total_score += info["score"]
average_score = total_score / len(students_dict)

print(f"班级平均分：{average_score:.2f}")
