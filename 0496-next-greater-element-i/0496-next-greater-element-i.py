class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Maps: number -> its next greater element
        next_greater_map = {}
        stack = []  # Monotonic decreasing stack
        
        # Step 1: Process nums2 to find next greater elements
        for num in nums2:
            # While the current number is greater than the top of the stack,
            # it means we found the "next greater element" for the stack's top.
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                next_greater_map[smaller_num] = num
            
            stack.append(num)
            
        # Step 2: Build the result for nums1 using our precomputed map
        # If a number isn't in the map, it defaults to -1
        return [next_greater_map.get(num, -1) for num in nums1]
                
                
                
        