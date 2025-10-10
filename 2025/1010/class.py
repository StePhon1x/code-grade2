# # while 猜数字游戏
# import random

# number = random.randint(1,100)
# guess = -1

# print("game begin =>")
# while guess != number:
#     guess = int(input("input your num:"))
#     if guess < number:
#         print("too small!")
#     elif guess > number:
#         print("too large!")
#     else:
#         print("bingo!")


# for
# 乘法表
# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i}x{j}={i*j}", end="\t")
#     print()

# 偶数检测
# i = 2
# s = 0
# a = []
# while i<=50:
#     a.append(i)
#     s += i
#     i += 2
# print(a)
# print(s/len(a))

# 字符串反转
str_h = "hello"
str_s = ""
for i in str_h:
    str_s = i + str_s
print(str_s)
