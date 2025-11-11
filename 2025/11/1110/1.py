n = int(input())

arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
x = 1
y = n // 2 + 1

for i in range(1, n * n + 1):
    arr[x][y] = i
    # 记录上一步的位置
    pre_x, pre_y = x, y
    # 尝试移动到右上角
    x -= 1
    y += 1
    # 越界处理
    if x < 1:
        x = n
    if y > n:
        y = 1
    # 如果那个格子已经被占
    if arr[x][y] != 0:
        x = pre_x + 1
        y = pre_y
        if x > n:
            x = 1

# 输出结果
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{arr[i][j]}", end=" ")
    print()
