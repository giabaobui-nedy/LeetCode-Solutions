class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_length = len(strs[0])
        for string in strs[1:]:
            the_len = len(string)
            if the_len < shortest_length:
                shortest_length = the_len
        result = ""
        for i in range(shortest_length):
            char = strs[0][i]
            print(char)
            for string in strs[1:]:
                if string[i] != char:
                    return result
            result += char
        return result



            