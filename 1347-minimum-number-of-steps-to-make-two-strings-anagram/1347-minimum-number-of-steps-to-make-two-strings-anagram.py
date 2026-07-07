from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)
        number_of_redundant_letters = 0
        for letter in string.ascii_lowercase:
            counter_of_that_letter_in_s = counter_s[letter]
            counter_of_that_letter_in_t = counter_t[letter]
            if counter_of_that_letter_in_t > counter_of_that_letter_in_s:
                number_of_redundant_letters += counter_of_that_letter_in_t - counter_of_that_letter_in_s
        return number_of_redundant_letters
           

