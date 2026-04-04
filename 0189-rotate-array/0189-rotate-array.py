class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # def calculate_final_index(first, k, length):
        #     print(first, k, length, (first + k) % length)
        #     return (first + k) % length
        # i = 0
        # length = len(nums)
        # while i < length:
        #     replaced_index = calculate_final_index(i, k, length)
        #     temp = nums[replaced_index]
        #     nums[replaced_index] = nums[i]
        #     i += 1
        length = len(nums)
        k = k % length
        # left_copy=nums[length-k:length]
        # right_copy=nums[0:length-k]
        nums[:] = nums[length-k:length] + nums[0:length-k]

       

        # for i, num in enumerate(nums):
        #     calculate_final_index(i, k, len(nums))
        #     print(num, " will be moved from ", i, " to ", calculate_final_index(i, k, len(nums)-1))
        