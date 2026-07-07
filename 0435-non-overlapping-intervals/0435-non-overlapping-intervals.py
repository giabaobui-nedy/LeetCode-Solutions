class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_interval = intervals.sort(key=lambda x: x[1])
        last_end = float('-inf')
        to_remove = 0
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                to_remove += 1
        return to_remove
                