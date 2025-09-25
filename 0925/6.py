# 给定列表
numbers = [5, 8, -7, 4, 6, 2, -3, 0]

# 提取最大元素
max_num = max(numbers)
print("最大元素为：", max_num)

# 删除最小元素
# 注意：如果列表中有多个最小值，`remove()` 只会删除第一个出现的
min_num = min(numbers)
numbers.remove(min_num)
print("删除最小元素后的列表：", numbers)

# 将负数的符号删除
# 使用列表推导式，对每个元素进行处理
# 如果元素小于0，则取其绝对值；否则保持原样
numbers = [abs(num) for num in numbers]
print("将负数符号删除后的列表：", numbers)