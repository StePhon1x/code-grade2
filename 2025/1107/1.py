"""
题目描述
现有一个长宽高分别为 w,x,h 组成的实心玻璃立方体，可以认为是由 1×1×1 的数个小方块组成的，每个小方块都有一个坐标 (i,j,k)。现在需要进行 q 次切割。每次切割给出 (x1,y1,z1),(x2,y2,z2) 这 6 个参数，保证 x1 ≤ x2，y1 ≤ y2，z1 ≤ z2；每次切割时，使用激光工具切出一个立方体空洞，空洞的壁平行于立方体的面，空洞的对角点就是给出的切割参数的两个点。

换句话说，所有满足 x1 ≤ i ≤ x2，y1 ≤ j ≤ y2，z1 ≤ k ≤ z2 的小方块 (i,j,k) 的点都会被激光蒸发。例如有一个 4×4×4 的大方块，其体积为 64；给出参数 (1,1,1),(2,2,2) 时，中间的 8 块小方块就会被蒸发，剩下 56 个小方块。现在想知道经过所有切割操作后，剩下的工艺品还剩下多少格小方块的体积？

输入格式
第一行三个正整数 w,x,h。
第二行一个正整数 q。
接下来 q 行，每行六个整数 (x1,y1,z1),(x2,y2,z2)。

输出格式
输出一个整数表示答案。
"""

w, x, h = map(int, input().split())
q = int(input())

# 初始化全1的立方体
cube = [[[1 for _ in range(h)] for _ in range(x)] for _ in range(w)]

for _ in range(q):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    # 坐标从1开始，所以减1转为Python的0索引
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            for k in range(z1 - 1, z2):
                cube[i][j][k] = 0  # 被激光蒸发

# 统计剩下多少格
remain = sum(sum(sum(layer for layer in row) for row in plane) for plane in cube)
print(remain)
