"""
题目1：编写一个安全的除法计算器函数 safe_divide(a, b)
要求：
1. 处理除数为0的情况
2. 处理输入非数字的情况
3. 使用try-except-else结构
4. 函数返回计算结果或错误信息
"""


def safe_divide(a, b):
    try:
        c = int(a) / int(b)
    except ZeroDivisionError:
        return "除数不能为0! "
    except ValueError:
        return "值必须为数字！"
    else:
        return f"{a} / {b} = {c}"


# 测试用例
print(safe_divide(10, 2))  # 应该输出: 5.0
print(safe_divide(10, 0))  # 应该输出适当的错误信息
print(safe_divide("10", "2"))  # 应该输出: 5.0
print(safe_divide("abc", 2))  # 应该输出适当的错误信息


"""
题目2：编写程序读取学生成绩文件 grades.txt，处理可能出现的异常：
1. 文件不存在异常
2. 文件内容格式错误（非数字成绩）
3. 统计平均分，忽略非法数据
文件内容示例：
张三 85
李四 92
王五 abc
赵六 78
"""


def calculate_average_grade(filename):
    total_score = 0
    avg = 0
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.readlines()
            for line_num, line in enumerate(content, 1):
                part = line.strip().split()
                if len(part) != 2:
                    print(f"忽略非法数据! 第{line_num}行数据出现错误！")
                name = part[0]
                score_str = part[1]
                try:
                    total_score += int(score_str)
                except ValueError:
                    print(
                        f"文件内容格式错误（非数字成绩）! 第{line_num}行数据出现错误！"
                    )
        avg = total_score / len(content)
    except FileNotFoundError:
        print("文件不存在！")
    return f"平均分为{avg}"


# 测试
print(calculate_average_grade("grades.txt"))

"""
题目3：设计一个BankAccount类，包含以下方法并处理异常：
1. __init__: 初始化账户，余额不能为负数
2. withdraw: 取款，余额不足时抛出异常
3. deposit: 存款，存款金额不能为负数
4. transfer: 转账给另一个账户，处理各种异常情况
"""


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        if initial_balance < 0:
            raise ValueError("余额不能为负数!")
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("此次取款操作非法！")
        if amount > self.balance:
            raise ValueError("余额不足! ")
        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额不能为负数或0! ")
        self.balance += amount

    def transfer(self, amount, target_account):
        if not isinstance(target_account, BankAccount):
            raise TypeError("目标账户必须是一个 BankAccount 实例。")
        if amount <= 0:
            raise ValueError("转账金额必须大于0！")
        try:
            self.withdraw(amount)

            target_account.deposit(amount)

            print("转账成功!")

        except ValueError as e:
            print(f"转账失败: {e}")

        except Exception as e:
            print(f"转账遇到未预期错误，可能导致资金不一致。错误: {e}")


# 测试
try:
    account1 = BankAccount("Alice", 1000)
    account2 = BankAccount("Bob", 500)
    account1.transfer(1500, account2)  # 应该抛出异常
except Exception as e:
    print(f"错误: {e}")

"""
题目4：编写函数 process_number_list(numbers)，处理包含各种类型元素的列表：
输入示例：[1, 2, "3", 4, "five", 6, [7], 8]
要求：
1. 遍历列表，只对数字或可转换为数字的字符串进行平方计算
2. 忽略无法处理的数据类型
3. 返回处理后的数字平方列表
4. 使用异常处理来过滤非法数据
"""


def process_number_list(numbers):
    last_sqrt_numbers = []
    for n in numbers:
        try:
            num = float(n)

            sqr = num * num

            if num == int(num):
                last_sqrt_numbers.append(int(sqr))
            else:
                last_sqrt_numbers.append(sqr)

        except (ValueError, TypeError):
            pass
    return last_sqrt_numbers


# 测试
test_list = [1, 2, "3", 4, "five", 6, [7], 8, "9.5"]
result = process_number_list(test_list)
print(result)  # 应该输出: [1, 4, 9, 16, 36, 64, 90.25]


# $ python -u "/d/code-grade2/2025/11/1128/exception-exp.py"
# 10 / 2 = 5.0
# 除数不能为0!
# 10 / 2 = 5.0
# 值必须为数字！
# 文件不存在！
# 平均分为0
# 转账失败: 余额不足!
# [1, 4, 9, 16, 36, 64, 90.25]
