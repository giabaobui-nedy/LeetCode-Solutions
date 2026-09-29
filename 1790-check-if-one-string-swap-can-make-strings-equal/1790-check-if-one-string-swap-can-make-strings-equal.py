class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False
        if not diff:
            return True                  # already equal, zero swaps
        if len(diff) == 1:
            return False                 # one mismatch cannot be fixed by a swap
        i, j = diff
        return s1[i] == s2[j] and s1[j] == s2[i]
                

