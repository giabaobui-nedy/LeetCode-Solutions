class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i, n = 0, len(intervals)
        start, end = newInterval

        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i+=1
        # print(result)

        while i < n and intervals[i][0] <= end:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i+=1
        result.append([start, end])
        # print(result)

        # 3. After: everything left is fully to the right.
        while i < n:
            result.append(intervals[i])
            i += 1
        # print(result)

        return result

        