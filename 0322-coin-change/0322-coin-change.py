class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. Initialize the history book with a "virtual infinity" (amount + 1)
        # because you can never need more coins than the amount itself (even using 1ct coins)
        dp = [amount + 1] * (amount + 1)
        
        # 2. Day Zero Seed: 0 coins needed to make an amount of 0
        dp[0] = 0
        
        # 3. Bottom-Up Iteration
        for i in range(1, amount + 1):  # For every sub-amount
            for coin in coins:          # Try every coin
                if i - coin >= 0:       # If the coin isn't too big
                    # Look back in history at dp[i - coin], and add 1 for the current coin
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        # If the target amount is still set to our "infinity", it's impossible
        return dp[amount] if dp[amount] != amount + 1 else -1