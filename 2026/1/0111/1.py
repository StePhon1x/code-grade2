class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = nums.sort()
        for i in range(len(nums_sorted)-1):
            n = 0
            if nums_sorted[i]+1 == nums_sorted[i+1]:
                n += 1
            elif nums_sorted[i] == nums_sorted[i+1]:
                