class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        cur_start, cur_end = intervals[0]
        for i_start, i_end in intervals[1:]:
            if cur_end < i_start:
                ans.append([cur_start, cur_end])
                cur_start, cur_end = i_start, i_end
            else:
                cur_end = max(cur_end, i_end)
        ans.append([cur_start, cur_end])
        return ans

        