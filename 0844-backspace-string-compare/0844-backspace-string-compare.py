class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_final_string(s: str) -> str:
            stack = []
            for char in s:
                if char is "#":
                    if stack:
                        stack.pop()
                    continue
                else:
                    stack.append(char)
            return "".join(stack)
        s1 = build_final_string(s)
        t1 = build_final_string(t)

        return s1 == t1