from collections import Counter
# import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies of each number
        counts = Counter(nums)
        # Extract the k keys with the highest frequency values
        return heapq.nlargest(k, counts, key=counts.get)
        