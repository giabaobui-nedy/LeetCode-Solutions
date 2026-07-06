class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        # stack = []
        for ind, num1 in enumerate(nums1):
            start_search = False
            for num2 in nums2:
                if num2 == num1:
                    start_search = True
                    continue
                
                if not start_search:
                    continue
                
                if num2 > num1:
                    result[ind] = num2
                    break
        return result
                
                
                
        