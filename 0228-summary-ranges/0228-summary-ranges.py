class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        for num in nums:
            if result and num == result[-1][1] + 1:
                result[-1][1] = num
            else:
                result.append([num, num])
        for i, (start, end) in enumerate(result):
            if start == end:
                result[i] = f"{start}"
            else:
                result[i] = f"{start}->{end}"
        return result