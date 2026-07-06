class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for ind, temp in enumerate(temperatures):
            # peek at the top
            while stack and temp > temperatures[stack[-1]]:
                prev_temp_id = stack.pop()
                answer[prev_temp_id] = ind - prev_temp_id
            stack.append(ind)
        return answer


