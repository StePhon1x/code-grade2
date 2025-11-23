file = open("example.txt", "w")


with open("./example1.txt", "w", encoding = "utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")
f.close()

lines = ["第一行\n", "第二行\n", "第三行\n"]
with open("./example2.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

with open("./example2.txt", "r", encoding = "utf-8") as f:
    content = f.read()
    print("全部内容:", content)

with open("./example2.txt", "r", encoding = "utf-8") as f:
    content = f.read(4)
    print("前4:", content)
    content = f.read()
    print("剩余内容:", content)

with open("./example2.txt", "r", encoding = "utf-8") as f:
    line = f.readline()
    print("第一行:", line)
    line = f.readline(2)
    print("下一行前2个字符:", line)

with open("./example2.txt", "r", encoding = "utf-8") as f:
    lines = f.readlines()
    print("所有行:", lines)






import os
print(os.getcwd())

os.mkdir("ostest")
os.chdir("ostest")
print(os.getcwd())
os.mkdir("mktest")

f = open("1.txt", "w")
f.close()
os.rename("1.txt", "2.txt")
print(os.listdir("./"))

os.rmdir("./mktest")
print(os.listdir("./"))

os.remove("./2.txt")
print(os.listdir("./"))







import os.path
print(os.path.abspath("ostest"))
print(os.path.split(os.path.abspath("ostest")))
print(os.path.splitext("example.txt"))
print(os.path.exists("ostest"))
print(os.path.getsize("example2.txt"))

import shutil
shutil.copy("./example2.txt", "./example2_copy.txt")
shutil.copytree("./ostest", "./ostest_backup")
shutil.rmtree("./ostest_backup")
print(os.getcwd())
