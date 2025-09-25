# 定义杨辉三角的行数
rows = 6

# 初始化一个二维列表来存储杨辉三角的数据
triangle = []

# 循环生成每一行
for i in range(rows):
    # 每一行初始化为一个列表，初始元素为1
    row = [1]
    # 如果当前行不是第一行，则计算中间的元素
    if i > 0:
        for j in range(1, i):
            # 当前行第j个元素 = 上一行第j-1个元素 + 上一行第j个元素
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # 当前行的最后一个元素为1
        row.append(1)
    # 将当前行添加到杨辉三角列表中
    triangle.append(row)

# 打印杨辉三角
for row in triangle:
    print(' '.join(map(str, row)))