class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { '(' : ')', '{' : '}', '[': ']'}
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) == 0 or char != pairs[stack[-1]]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0