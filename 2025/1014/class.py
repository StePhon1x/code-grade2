# 猜数字

# 生成随机数
import random
number = random.randint(1, 10)

print("Begin->")
while True:
    guess = int(input("Please input the number:"))
    if guess == number:
        print("Bingo!")
        break
    else:
        print("Wrong, please try again!")
