class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        new_set = set(nums)
        missing_num = 1
        while missing_num in new_set:
            missing_num += 1
        return missing_num

        