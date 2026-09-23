class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Lowercase the string and keep only alphanumeric characters
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        print(cleaned)
        string_length = len(cleaned)
        left, right = 0, string_length - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True