class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        increasing_temp_stack = []
        for ind, temp in enumerate(temperatures):
            # peek at the top
            while increasing_temp_stack and temp > increasing_temp_stack[-1][1]:
                prev_temp_id, _ = increasing_temp_stack.pop()
                answer[prev_temp_id] = ind - prev_temp_id
            increasing_temp_stack.append((ind, temp))
        return answer


