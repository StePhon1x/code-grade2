# 字符串查找与验证
# text = "Hello Python 2024 Python"

# 1. find() rfind() 查找子串位置 左侧右侧
# 查找的是相同字符串的第一个位置
# print(text.find("Python"))
# print(text.find("Java")) # 找不到会输出-1
# rfind()从右往左找
# print(text.rfind("java"))
# print(text.rfind("Python"))

# 2. index() rindex() 查找字串位置 左侧右侧 找不到报错
# print(text.index("Python"))
# print(text.index("Java")) # 报错
# print(text.rindex("Python"))
# print(text.rindex("Java")) # 报错

# 3. count() 统计字串出现次数
# print(text.count("o"))
# print(text.count("l"))
# print(text.count("Java"))

# 4. startswith() - 检查开头
# print(text.startswith("Hello"))
# print(text.startswith("Java"))

# 5. endswith() - 检查结尾
# print(text.endswith("Hello"))
# print(text.endswith("Python"))

# 6. isalnum(), isalpha(), isdigit() - 检查字符串内容
# print("abc123".isalnum()) # True - 只有字母和数字
# print("abc 123".isalnum()) # False - 包含空格
# print("abc".isalpha()) # True - 只有字母
# print("abc123".isalpha()) # False - 包含数字
# print("123".isdigit()) # True - 只有数字
# print("123abc".isalpha()) # False - 包含字母

# 7. islower(), isupper(), isspace()
# print("hello".islower()) # True - 全小写
# print("Hello".islower()) # False - 有大写字母
# print("WORLD".isupper()) # True - 全大写
# print("World".isupper()) # False - 有小写字母
# print("  ".isspace()) # True - 全是空格
# print("  a  ".isspace()) # False - 有字母


# 验证用户名是否合法
# def validate_username(username):
#     if not 5 <= len(username) <= 15:
#         return False
#     if username[0].isdigit():
#         return False
#     for le in username:
#         if not (le.isalnum() or le == "_"):
#             return False
#     return True

# # 测试用例
# print(validate_username("user_123")) #
# print(validate_username("user@name"))




# 判断密码强度
# 弱：len < 8 or isalpha() or isdigit()
# 中：len >= 8, isalnum() or not isalpha() isdigit()
# 强：len >= 8, isalnum() and not isalpha() isdigit()

def check_password_strength(password):
    if len(password) < 8 :
        return "弱"
    else:
        le_letter = False
        le_digit = False
        le_special = False
        for le in password:
            if le.isalpha():
                le_letter = True
            elif le.isdigit():
                le_digit = True
            else:
                le_special = True

        if le_letter and le_digit and le_special:
            return "强"
        elif le_letter and le_digit:
            return "中"
        elif le_letter and le_special:
            return "中"
        else:
            return "弱"

# 测试
print(check_password_strength("ABCabc123!"))
