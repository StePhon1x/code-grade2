# 定义数字的 3x5 点阵 (X = 亮点, . = 暗点)
digits = {
    "0": ["XXX", "X.X", "X.X", "X.X", "XXX"],
    "1": ["..X", "..X", "..X", "..X", "..X"],
    "2": ["XXX", "..X", "XXX", "X..", "XXX"],
    "3": ["XXX", "..X", "XXX", "..X", "XXX"],
    "4": ["X.X", "X.X", "XXX", "..X", "..X"],
    "5": ["XXX", "X..", "XXX", "..X", "XXX"],
    "6": ["XXX", "X..", "XXX", "X.X", "XXX"],
    "7": ["XXX", "..X", "..X", "..X", "..X"],
    "8": ["XXX", "X.X", "XXX", "X.X", "XXX"],
    "9": ["XXX", "X.X", "XXX", "..X", "XXX"],
}

# 输入
n = int(input())  # 数字位数（其实用不到，但题目格式要求）
s = input().strip()  # 输入数字字符串

# 输出拼接
rows = [""] * 5  # 用来拼接每一行
for ch in s:
    for i in range(5):
        rows[i] += digits[ch][i] + "."  # 每个数字之间加一列间隔点

# 输出结果（去掉最后多余的'.'）
for r in rows:
    print(r[:-1])
