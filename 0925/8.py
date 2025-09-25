import os
import shutil

# 指定源目录和目标目录
src_dir = 'd:\\code-grade2\\0925'  # 修改为实际存在的目录
dst_dir = 'my_python'

# 如果目标文件夹不存在，则创建它
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# 遍历源目录中的文件
for file_name in os.listdir(src_dir):
    # 只处理扩展名为 .py 的文件
    if file_name.endswith('.py'):
        src_file_path = os.path.join(src_dir, file_name)
        dst_file_path = os.path.join(dst_dir, file_name)
        # 执行文件复制操作
        shutil.copy(src_file_path, dst_file_path)

print("所有Python文件已从 {} 复制到 {}。".format(src_dir, dst_dir))