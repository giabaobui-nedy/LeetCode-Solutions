class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j, c in enumerate(typed):
            if i < len(name) and c == name[i]:
                i += 1
            elif j > 0 and c == typed[j - 1]:
                continue  # long press of the last key
            else:
                return False
        return i == len(name)
