class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pointer = round((right - left) / 2)
        while left < pointer < right:
            # binary search
            if nums[pointer] > target:
                right = pointer
            elif nums[pointer] < target:
                left = pointer
            else:
                return pointer
            pointer = round(((right - left) / 2) + left)
        if target == nums[left]:
            return left
        if target == nums[right]:
            return right
        if target < nums[left]:
            return 0
        if nums[left] < target < nums[right]:
            return left + 1
        if target > nums[right]:
            return right + 1
          