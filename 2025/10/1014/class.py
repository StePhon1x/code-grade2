# # 猜数字

# # 生成随机数
# import random
# number = random.randint(1, 10)

# print("Begin->")
# while True:
#     guess = int(input("Please input the number:"))
#     if guess == number:
#         print("Bingo!")
#         break
#     else:
#         print("Wrong, please try again!")

# 打印输入的字母列表 不包括quit
# words = []
# while True:
#     word = input("Please input the word: ")
#     if word == "quit":
#         print(words)
#         break
#     else:
#         print()
#         words.append(word)


# 输出1到20之间3的倍数
# 不使用continue
# for num in range(1,21):
#     if num % 3 == 0:
#         print(num)

# # 使用continue
# for num in range(1, 21):
#     if num % 3 != 0:
#         continue
#     print(num)

# 用for循环统计字符串中每个字符出现的次数
word_count = {}

# 使用get方法
for w in input("Please input the word: "):
    word_count[w] = word_count.get(w, 0) + 1
print(word_count)



# 不使用get方法 if...else
for w in input("Please input the word: "):
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1
print(word_count)

# 不使用get方法 try...except
for w in input("Please input the word: "):
    try:
        word_count[w] += 1
    except KeyError:
        word_count[w] = 1
print(word_count)