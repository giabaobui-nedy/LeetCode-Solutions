class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start
        intervals.sort()

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            
            if start <= last_end:
                merged[-1] = [merged[-1][0], max(merged[-1][1], end)]
            else:
                merged.append([start, end])

        return merged

        