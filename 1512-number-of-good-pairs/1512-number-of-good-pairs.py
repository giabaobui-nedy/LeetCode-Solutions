class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        seen = {}
        pairs = 0
        for num in nums:
            pairs += seen.get(num, 0)          # pairs with every earlier copy
            seen[num] = seen.get(num, 0) + 1   # now record this copy
        return pairs         