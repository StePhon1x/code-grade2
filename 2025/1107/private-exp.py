"""
这是一个简单的银行账户管理系统，通过SwitzerlandBankAccount类来模拟银行账户的基本操作。主要考察私有属性和私有方法的概念和应用。
该程序实现了一个银行账户类，包含以下功能：
变量和方法：
私有变量：
__balance：账户余额（外部无法直接访问）
__account_holder：账户持有人姓名

公有方法：
deposit(amount)：存款方法，增加账户余额，只有有效金额（正数）才会被接受
withdraw(amount)：取款方法，减少账户余额，只有有效金额（正数且不超过余额）才会被接受
get_balance()：获取当前账户余额
私有方法：
__validate_deposit_amount(amount)：验证存款金额是否合法（正数）
__validate_withdraw_amount(amount)：验证取款金额是否合法（正数且不超过当前余额）

"""


class SwitzerlandBankAccount:

    # 初始化账户
    def __init__(self, balance, account_holder):
        self.__balance = balance
        self.__account_holder = account_holder

    # 存款行为
    def deposit(self, amount):
        if self.__validate_deposit_amount(amount):
            self.__balance += amount

    # 取款行为
    def withdraw(self, amount):
        if self.__validate_withdraw_amount(amount):
            self.__balance -= amount

    # 读取账户余额
    def get_balance(self):
        return f"当前余额:{self.__balance}"

    # 验证存款金额是否合法（正数）
    def __validate_deposit_amount(self, amount):
        if amount <= 0:
            print(f"本次存款{amount}行为不合法!")
            return False
        return True

    # 验证取款金额是否合法（正数且不超过当前余额）
    def __validate_withdraw_amount(self, amount):
        if amount > self.__balance or amount <= 0:
            print(f"本次取款{amount}行为不合法!")
            return False
        return True


# 测试代码
account = SwitzerlandBankAccount(1000, "Alice")
account.deposit(0)
account.deposit(-100)
account.deposit(500)
print(account.get_balance())

account.withdraw(2000)
account.withdraw(-50)
account.withdraw(300)
print(account.get_balance())
