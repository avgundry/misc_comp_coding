from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        while coins[-1] > amount:
            coins.pop() 

        dp = [[-1 for _ in range(len(coins))] for _ in range(amount)]

        return self.recurse(amount, coins, len(coins) - 1)

    def recurse(self, amount, coins, dp, i):
        if dp[amount][i] != -1:
            return dp[amount][i]
        dp[amount][i] = 0
        total = 0
        if i >= 0:
            j = 0
            while coins[i] * j <= amount:
                total += self.recurse(amount - coins[i] * j, coins, i - 1)
                j += 1
        return total

if __name__ == "__main__":
    s = Solution()
    print(s.change(5, [1, 2, 5]))
    print(s.change(10, [10]))

