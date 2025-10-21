# 字符串分割与连接方法

#  1. split() - 分割字符串 | rsplit() - 从右侧分割字符串
# sentence = "Hello World Hello Python"
# languages = sentence.split(" ")
# print(languages)

# sentence = "Python,Java,C++,JavaScript"
# languages = sentence.split(",")
# print(languages)

# data = "apple|banana|cherry|date"
# fruits = data.rsplit("|",2) # 最多分割成3个部分
# print(fruits)

#  2. partiton(), rpartition() - 按第一个/最后一个分隔符分割
# url = "https://www.example.com/path"
# head, sep, tail = url.partition("://")
# print(url.partition("://"))
# print(head)
# print(sep)
# print(tail)

# head, sep, tail = url.rpartition("/")
# print(url.rpartition("/"))
# print(head)
# print(sep)
# print(tail)

# 3. join() - 连接字符串（split（）的逆操作)
# split   string -> list
# join    list -> string
# words = ["Hello", "world", "from", "Python"]
# sentence = " ".join(words)
# print(sentence)

# words = ["Hello", "world", "from", "Python"]

# import time
# start = time.time()
# sentence = " ".join(words)
# end = time.time()
# print(f"Join:{end - start:.6f}s")

# start = time.time()
# sentence = ""
# for word in words:
#     sentence += word + " "
# end = time.time()
# print(f"conce:{end - start:.6f}s")



def analyze_file_path(file_path):
    path = file_path.rpartition("/")
    filename = path[2]
    ex = path[2].rsplit(".")[-1]
    extension = ex
    dir_path = path[0]    
    
    
    
    return {
        "filename": filename,
        "extension": extension,
        "directory": dir_path
    }


data = "2024 - "






















