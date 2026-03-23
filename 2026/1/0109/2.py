class Solution:
    def twoSum(self, nums, target):
        a = 0
        b = 0
        for n in nums:
            n_1 = target - n
            if n_1 in nums and n_1 != n:
                a = nums.index(n)
                b = nums.index(n_1)
                break
        return [a, b]

if __name__ == "__main__":
    nums_input = input().strip()
    nums_clean = nums_input.replace('[', '').replace(']', '').replace(' ', '')
    nums = list(map(int, nums_clean.split(',')))
    
    target = int(input())
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)
