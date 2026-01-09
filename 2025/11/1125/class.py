# try:
#     a = float(input("请输入被除数: "))
#     b = float(input("请输入除数: "))
#     c = a/b
#     print("商为:", c)
# except ZeroDivisionError:
#     print("除数不能为0! ")
# 一句话总结： 捕获并处理特定的除零异常 (ZeroDivisionError)。

# try:
#     a = float(input("请输入被除数: "))
#     b = float(input("请输入除数: "))
#     c = a/b
#     print("商为:", c)
# except ZeroDivisionError:
#     print("除数不能为0! ")
# except ValueError:
#     print("被除数和除数应为数值类型! ")
# 一句话总结： 使用多个 except 块分别处理不同类型的特定异常。

# try:
#     a = float(input("请输入被除数: "))
#     b = float(input("请输入除数: "))
#     c = a/b
#     print("商为:", c)
# # except (ZeroDivisionError, ValueError):
# #     print("捕获到异常!")
# except (ZeroDivisionError, ValueError) as r:
#     print("捕获到异常: %s" %r)
# 一句话总结： 将多种异常类型合并捕获，并使用 `as r` 获取异常对象信息。

# try:
#     a = float(input("请输入被除数: "))
#     b = float(input("请输入除数: "))
#     c = a/b
#     print("商为:", c)
# # except:
# #     print("出错了！")
# except Exception as r:
#     print("捕获到异常：%s"%r)
# 一句话总结： 使用基类 `Exception` 捕获所有运行时异常并打印其描述信息。

# 同时包含多个except, else, 和finally语句
# try:
#     a = float(input("请输入被除数: "))
#     b = float(input("请输入除数: "))
#     c = a/b
#     print("商为:", c)
# except ZeroDivisionError:
#     print("除数不能为0！")
# except ValueError:
#     print("被除数和除数应为数值类型！")
# except:
#     print("其他错误!")
# else:
#     print("没有错误！")
# finally:
#     print("运行结束！")
# 一句话总结： 演示了 `try-except-else-finally` 完整的异常处理结构和执行顺序。

# raise NameError('用户名太长了')
# # 输出：
# # NameError: 用户名太长了