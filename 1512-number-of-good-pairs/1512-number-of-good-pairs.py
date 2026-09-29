class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 0
        return sum((n * (n + 1)) // 2 for n in count.values())                