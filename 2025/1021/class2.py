# 字符串转换与清洗方法


text = "Hello WORLD"

# 1. lower()/upper()/capitalize()/title()/swapcase() - 改变大小写
# print(text.lower()) # hello world
# print(text.upper()) # HELLO WORLD
# print(text.capitalize()) # Hello world
# print(text.title()) # Hello World
# print(text.swapcase()) # hELLO world

# 2. replace() - 替换内容
# print(text.replace("WORLD", "Python")) # Hello Python

# 3. strip()/lstrip()/rstrip() - 去除空白字符
# text = "    Hello WORLD     \n"
# print(text.strip(),"#")
# print(text.lstrip(),"#")
# print(text.rstrip(),"#")

# 4. maketrans() + translate() - 字符映射转换
# table = str.maketrans("aeiou", "12345")
# print("Hello".translate(table))






def clean_and_format(data_list):
    clean_list = []
    for data in data_list:
        data = data.strip()
        data = data.lower()
        data = data.replace("_", " ")
        clean_list.append(data)
    result = "|".join(clean_list)
    return result


data = ["    Python_Programing   ", ""]




