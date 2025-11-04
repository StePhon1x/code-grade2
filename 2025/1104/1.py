l, m = map(int, input().split())
tree = [False] * (l + 1)

for _ in range(m):
    le, ri = map(int, input().split())
    for j in range(le, ri + 1):
        tree[j] = True  # 被砍掉

print(tree.count(False))
