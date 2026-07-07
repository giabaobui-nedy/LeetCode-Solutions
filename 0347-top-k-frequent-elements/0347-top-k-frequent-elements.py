from collections import Counter
# import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [element for element, _ in Counter(nums).most_common(k)]
        