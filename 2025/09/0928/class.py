# '''
# if 语句
# '''
# # 示例1： 年龄判断
# age = 20 
# if age >= 18:
#     print("您已成年")

# #  示例2： 成绩合格判断
# score = 85
# if score >= 60:
#     print("成绩及格")
#     print("恭喜通过考试")

# '''
# if else
# '''
# # 示例1： 奇偶数判断
# number  = 7
# if number %2 ==0:
#     print(f"{number}是偶数")
# else:
#     print(f"{number}是奇数")

# #  精简形式
# print(f"{number}是偶数") if number %2 == 0 else print(f"{number}是奇数")

# #  示例2： 登录验证
# username = input("请输入用户名：")
# password = input("请输入密码：")
# if username == "admin" and password == "123456":
#     print("登录成功")
# else:
#     print("用户名或密码错误！")



# '''
# if - elif - else
# '''
# #  示例1： 成绩等级评定
# score = 85
# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("良好")
# elif score >= 70:
#     print("中等")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")


# '''
# match - case 结构 (Python 3.10+)
# '''
# # 示例1： 简单的值匹配
# status = 404
# match status:
#     case 200:
#         print("成功")
#     case 404:
#         print("未找到")
#     case 500:
#         print("服务器错误")
#     case _:
#         print("未知状态")
        
        
# # 示例2： 多个值匹配
# command = "start"
# match command:
#     case "start" | "run":
#         print("启动程序")
#     case "stop" | "exit":
#         print("停止程序")
#     case _:
#         print("未知命令")

# temperature = int(input())
# if temperature > 35:
#     print("红色高温预警")
# elif 30 <= temperature <= 35:
#     print("橙色高温预警")
# elif 25 < temperature <= 29:
#     print("适宜温度")
# elif temperature <= 25:
#     print("注意保暖")


# x = float(input("输入第一个数字："))
# y = float(input("输入第二个数字："))
# operator = input("请输入运算符 (+, -, *, /): ")
# if operator == '+':
#     result = x + y
#     print(f"{x} + {y} = {result}")
# elif operator == '-':
#     result = x - y
#     print(f"{x} - {y} = {result}")
# elif operator == '*':
#     result = x * y
#     print(f"{x} * {y} = {result}")
# elif operator == '/':
#     if y != 0:
#         result = x / y
#         print(f"{x} / {y} = {result}")
#     else:
#         print("错误，除数不能为零。")


# n = int(input("请输入数字："))
# match n:
#     case 1:
#         print("星期一")
#     case 2:
#         print("星期二")
#     case 3:
#         print("星期三")
#     case 4:
#         print("星期四")
#     case 5:
#         print("星期五")
#     case 6:
#         print("星期六")
#     case 7:
#         print("星期日")
#     case _:
#         print("输入错误")


grade = int(input("请输入成绩："))
if 95 <= grade <= 100:
    s = 4.5
    if grade == 100:
        print("为满分")
elif 90 <= grade <= 94:
    s = 4.0
elif 85 <= grade <= 89:
    s = 3.5
elif 80 <= grade <= 84:
    s = 3.0
elif 78 <= grade <= 79:
    s = 2.8
elif 75 <= grade <= 77:
    s = 2.5
elif 73 <= grade <= 74:
    s = 2.3
elif 70 <= grade <= 72:
    s = 2.0
elif 68 <= grade <= 69:
    s = 1.8
elif 65 <= grade <= 67:
    s = 1.5
elif 63 <= grade <= 64:
    s = 1.3
elif 60 <= grade <= 62:
    s = 1.0
else:
    s = 0.0
print(s)





















