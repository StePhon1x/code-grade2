# 字符串格式化与排版方法

# 1. format() - 格式化输出
# 占位符
name = "Alice"
age = 25

message1 = "我叫{}, 今年{}岁".format(name, age)
message2 = "我叫{0}, 今年{1}岁".format(name, age)
message3 = "我叫{n}, 今年{a}岁"

# 2. center()/ljust()/rjust() - 字符串对齐
title = "Python教程"


# 3. eval() - 字符串转代码（谨慎使用）
result = eval("3 + 5 * 2")
