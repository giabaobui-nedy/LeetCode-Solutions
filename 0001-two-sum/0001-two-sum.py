class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for ind, num in enumerate(nums):
            a_number_needed = target - num
            if a_number_needed in hash_map:
                return [hash_map[a_number_needed], ind]
            else:
                hash_map[num] = ind
                


        