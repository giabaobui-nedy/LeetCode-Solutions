from collections import deque
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        queue = deque()
        for char in s:
            queue.append(char)
        for i in range(len(t)):
            if queue and t[i] == queue[0]:
                queue.popleft()
        return not queue



        