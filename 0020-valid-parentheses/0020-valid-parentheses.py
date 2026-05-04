class Solution(object):
    def isValid(self, s):
        parenthesis_dict = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in parenthesis_dict:
                stack.append(char)
            else:
                if not stack or char != parenthesis_dict[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0

        


        