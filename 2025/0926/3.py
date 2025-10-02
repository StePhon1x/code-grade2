# 读入并限制范围
while True:
    a = int(input())
    if 1 <= a <= 1_000_000_000:
        break

# 计算“除以 2 直到小于 1”的次数
n = 0
while a >= 1:
    a //= 2
    n += 1

print(n)