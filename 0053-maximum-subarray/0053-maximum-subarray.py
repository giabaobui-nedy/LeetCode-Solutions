class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = nums[0]
        max_ending = nums[0]
        for i in range(1, len(nums)):
            max_ending = max(max_ending + nums[i], nums[i])
            max_val = max(max_val, max_ending)
        return max_val

            





        
        