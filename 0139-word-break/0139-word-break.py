class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # for fast "is this a word?" checks
        n = len(s)
        
        # dp[i] = "can I successfully break the first i characters of s?"
        dp = [False] * (n + 1)
        dp[0] = True  # zero characters = nothing to break = automatically true

        for i in range(1, n + 1):          # for every possible "end point"
            for j in range(i):              # try every possible "cut point" before it
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True   # found a valid way to reach position i!
                    break

        return dp[n]  # can I break the WHOLE string?
        