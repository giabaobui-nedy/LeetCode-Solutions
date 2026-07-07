from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)
        number_of_flex_char = 0
        for letter in string.ascii_lowercase:
            if counter_t[letter] > counter_s[letter]:
                number_of_flex_char += counter_t[letter] - counter_s[letter]
        return number_of_flex_char
           

