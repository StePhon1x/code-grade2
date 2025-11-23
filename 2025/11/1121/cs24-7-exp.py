"""
题目一：文本文件读写与指针操作
要求：
    1.创建一个名为story.txt的文本文件，写入以下内容：
        从前有座山，山里有座庙。
        庙里有个老和尚在讲故事。
        讲的是什么故事呢？
    2.使用seek()和tell()方法：
        读取并打印文件的前10个字符
        将文件指针移动到第15个字符位置，读取并打印接下来的10个字符
        返回到文件开头，读取并打印第一行内容
        在每一步操作后，打印当前的文件指针位置
"""

# lines = ["从前有座山，山里有座庙。\n", "庙里有个老和尚在讲故事。\n",  "讲的是什么故事呢？\n"]
# with open("./story.txt", "w", encoding = "utf-8") as f:
#     f.writelines(lines)

# with open("./story.txt", "r", encoding = "utf-8") as f:
#     line = f.read(10)
#     print(line)
#     p = f.tell()
#     print("当前的文件指针位置:", p)
#     f.seek(15)
#     line = f.read(10)
#     print(line)
#     p = f.tell()
#     print("当前的文件指针位置:", p)
#     f.seek(0)
#     first_line = f.readline()
#     print(first_line)
#     p = f.tell()
#     print("当前的文件指针位置:", p)

"""
题目二：文本文件读写与os模块
要求：
    使用os模块创建一个名为logs的目录
    在该目录下创建三个名为app1.log、app2.log、app3.log的日志文件
    分别向三个日志文件中写入一条日志记录，每条记录包含内容“这是第n条日志”
    使用os模块列出logs目录中的所有文件，并读取日志文件内容打印出来
"""

# import os


# # os.mkdir("logs")
# os.chdir("logs")

# with open("app1.log", "w", encoding="utf-8") as a1, \
#     open("app2.log", "w", encoding="utf-8") as a2, \
#     open("app3.log", "w", encoding="utf-8") as a3:
#         a1.write("这是第1条日志\n")
#         a2.write("这是第2条日志\n")
#         a3.write("这是第3条日志\n")

# print(os.listdir("."))

# for f in sorted(f for f in os.listdir(".") if f.endswith(".log")):
#     print(f"\n=== {f} ===")
#     with open(f, "r", encoding="utf-8") as file:
#         print(file.read().rstrip() or "（空文件）")


"""
题目三：os和os.path模块应用
要求：  
    1.使用os模块创建以下目录结构,并在main.py、utils.py和input.txt文件中写入简单内容：
        project/
        ├── src/
        │   ├── main.py     (内容 # 主程序文件\n)
        │   └── utils.py    (内容 # 工具函数文件\n)
        └── data/
            └── input.txt   (内容 输入数据\n)
    2.使用os.path模块完成以下任务：
        检查project/src/main.py文件是否存在
        获取project/data/input.txt文件的绝对路径
        检查project目录是否是目录而非文件
        获取project目录下所有子目录和文件的名称
"""

# import os
# import os.path
# from pathlib import Path

# base_dir = Path(__file__).parent.resolve()

# output_dir = base_dir / "project"
# output_dir.mkdir(exist_ok=True)

# (output_dir / "src").mkdir(exist_ok=True)
# (output_dir / "data").mkdir(exist_ok=True)

# (output_dir / "src" / "main.py").write_text("主程序文件\n", encoding="utf-8")
# (output_dir / "src" / "utils.py").write_text("工具函数文件\n", encoding="utf-8")
# (output_dir / "data" / "input.txt").write_text("输入数据\n", encoding="utf-8")

# project_root = os.path.dirname(os.path.abspath(__file__))

# main_py_path = os.path.join(project_root, "project", "src", "main.py")
# print(f"[1] main.py文件是否存在:{os.path.exists(main_py_path)}")

# input_txt_path = os.path.join(project_root, "project", "data", "input.txt")
# abs_input_path = os.path.abspath(input_txt_path)
# print(f"[2] input.txt 的绝对路径：{abs_input_path}")

# project_path = os.path.join(project_root, "project")
# if os.path.exists(project_path):
#     if os.path.isdir(project_path):
#         print("[3] project目录是目录而非文件")

# if os.path.isdir(project_path):
#     print("[4] project目录下所有子目录和文件的名称")
#     for root, dirs, files in os.walk(project_path):
#         # root  : 当前正在遍历的目录
#         # dirs  : 当前目录下的子目录名列表
#         # files : 当前目录下的文件名列表

#         # 打印当前目录（可读性更好）
#         rel_dir = os.path.relpath(root, project_root)   # 显示相对于项目根目录的路径
#         print(f"[{rel_dir}]")

#         for f in sorted(files):
#             file_path = os.path.join(root, f)
#             rel_path = os.path.relpath(file_path, project_root)
#             print(f"    ├── {f}   →   {rel_path}")
#         print()  # 空行分隔
# else:
#     print("project 目录不存在！")


"""
题目四：os与shutil模块应用
要求：
    创建一个名为source的目录，并在其中创建3个测试文件file1.txt、file2.txt、file3.txt，写入内容“这是文件n的内容”
    使用shutil模块完成以下任务：
        将source目录完整复制到backup目录
        将source目录中的file1.txt移动到moved_files目录
        删除source目录中的file2.txt文件
        输出source、backup和moved_files目录的内容
"""

import os
import shutil

# 如果之前运行过，先清理可能存在的目录（可选）
for dir_name in ["source", "backup", "moved_files"]:
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)

# 1. 创建 source 目录并在其中创建 3 个测试文件
os.mkdir("source")

for i in range(1, 4):
    file_name = f"source/file{i}.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(f"这是文件{i}的内容")

print("=== 创建初始文件 ===")
print("source 目录内容：", os.listdir("source"))

# 2. 使用 shutil 完成指定操作

# 将整个 source 目录复制到 backup 目录
shutil.copytree("source", "backup")
print("\n已将 source 完整复制到 backup")

# 创建 moved_files 目录并移动 file1.txt
os.mkdir("moved_files")
shutil.move("source/file1.txt", "moved_files/file1.txt")
print("已将 file1.txt 移动到 moved_files 目录")

# 删除 source 目录中的 file2.txt
os.remove("source/file2.txt")
print("已删除 source/file2.txt")

# 3. 输出最终各个目录的内容
print("\n" + "=" * 40)
print("最终目录状态：")
print("-" * 40)
print("source 目录内容：", os.listdir("source"))
for item in os.listdir("source"):
    with open(f"source/{item}", "r", encoding="utf-8") as f:
        print(f"   {item} → {f.read()}")

print("\nbackup 目录内容：", os.listdir("backup"))
for item in os.listdir("backup"):
    with open(f"backup/{item}", "r", encoding="utf-8") as f:
        print(f"   {item} → {f.read()}")

print("\nmoved_files 目录内容：", os.listdir("moved_files"))
for item in os.listdir("moved_files"):
    with open(f"moved_files/{item}", "r", encoding="utf-8") as f:
        print(f"   {item} → {f.read()}")


"""
题目五：pickle模块应用
要求：
    实例化创建一个Person类对象（张三，‘18’）
    创建一个包含多个不同类型对象（字典、列表、实例、字符串、整数、浮点数）的列表data_list
    使用pickle模块将该列表序列化并保存到文件example.pkl中
    从example.pkl文件中读取数据，并反序列化为原始对象，逐个打印每个对象及其类型
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"Person(name={self.name}, age={self.age})"


info = {"city": "北京", "country": "中国"}
simple_list = [10, 20, 30, 40]
simple_string = "Hello, pickle!"
simple_int = 100
simple_float = 3.14

import pickle


# 1. 实例化一个 Person 对象：张三，18岁（年龄用字符串'18'）
person = Person("张三", "18")


# 3. 创建包含多种不同类型对象的列表 data_list
data_list = [
    {"name": "Alice", "score": 95},  # 字典
    [1, 2, 3, "abc", True],  # 列表（含混合类型）
    person,  # Person 实例
    "这是一个中文字符串",  # 字符串
    42,  # 整数
    9.999,  # 浮点数
    info,  # 另一个字典
    simple_list,  # 简单列表
    simple_string,  # 英文字符串
    simple_int,  # 整数
    simple_float,  # 浮点数
]

# 4. 使用 pickle 将 data_list 序列化保存到文件 example.pkl
with open("example.pkl", "wb") as f:
    pickle.dump(data_list, f)

print("数据已成功序列化并保存到 example.pkl\n")

# 5. 从文件中读取并反序列化
with open("example.pkl", "rb") as f:
    loaded_data = pickle.load(f)

# 6. 逐个打印每个对象及其类型
print("=" * 50)
print("反序列化后的数据（共 {} 个元素）：".format(len(loaded_data)))
print("=" * 50)

for i, item in enumerate(loaded_data, 1):
    print(f"{i}. 值: {item}")
    print(f"   类型: {type(item)}")

    # 特殊处理 Person 对象，调用 show() 方法显示更友好信息
    if isinstance(item, Person):
        print(f"   → {item.show()}")
    print("-" * 40)
