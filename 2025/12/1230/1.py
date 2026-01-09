"""
题目背景
NOIP2014 普及 T1

题目描述
珠心算是一种通过在脑中模拟算盘变化来完成快速运算的一种计算技术。珠心算训练，既能够开发智力，又能够为日常生活带来很多便利，因而在很多学校得到普及。

某学校的珠心算老师采用一种快速考察珠心算加法能力的测验方法。他随机生成一个正整数集合，集合中的数各不相同，然后要求学生回答：其中有多少个数，恰好等于集合中另外两个（不同的）数之和？

最近老师出了一些测验题，请你帮忙求出答案。

输入格式
共两行，第一行包含一个整数 n，表示测试题中给出的正整数个数。

第二行有 n 个正整数，每两个正整数之间用一个空格隔开，表示测试题中给出的正整数。

输出格式
一个整数，表示测验题答案。
"""

n = int(input())

numbers = input()
arr = list(map(int, numbers.split()))
arr.sort()

count = 0

for i in range(len(arr)):
    target = arr[i]
    for j in range(i):
        y = arr[j]
        z = target - y

        if z in arr and y != z:
            count += 1
            break
print(count)
