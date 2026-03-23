from collections import defaultdict  # 导入defaultdict，用于创建默认值为list的字典

class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = defaultdict(list)  # 创建一个默认值为list的字典，用于存储分组结果

        for str in strs:  # 遍历输入的字符串列表
            sorted_str = ''.join(sorted(str))  # 对字符串进行排序，并将其转换为字符串作为键
            anagram_dict[sorted_str].append(str)  # 将原字符串添加到对应的分组中

        return list(anagram_dict.values())  # 返回字典的值，即分组后的列表

solution = Solution()
strs = list(input().split(","))
print(solution.groupAnagrams(strs))

