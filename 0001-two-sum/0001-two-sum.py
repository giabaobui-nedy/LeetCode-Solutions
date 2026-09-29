class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        di = {}
        for i, num in enumerate(nums):
            if (target - num) in di:
                return [di[target - num], i]
            else:
                di[num] = i
        