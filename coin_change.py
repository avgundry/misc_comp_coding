from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Bottom-up DP approach."""
        # Ugh this is difficult...
        # Let's have dp[i] be the min # of coins to get to amount i.
        # Then go forward from dp[0]

        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]


        



        """Brute force recursion approach - find all paths."""
    #     paths = []
    #     self.recurse(coins, amount, paths, [])
    #     if paths:
    #         return len(sorted(paths, key=lambda x:len(x))[0])

    #     return -1
    
    # def recurse(self, coins, amount, paths, path):
    #     if amount == 0:
    #         paths.append(path)
        
    #     for coin in coins:
    #         if coin <= amount:
    #             print(f"subtracting {coin} from {amount}, new path is {path.copy() + [coin]}")
    #             self.recurse(coins, amount - coin, paths, path.copy() + [coin])


        
        # # Seems like a simple, greedy algorithm.
        # # ah...I see. Won't always include 1 so we can't always do it.
        # coins.sort()
        # i = len(coins) - 1
        # num = 0
        # print(f"coins: {coins}")
        # while amount > 0 and i > -1:
        #     print(f"index {i}")
        #     print(f"current amount: {amount}")
        #     print(f"current coin: {coins[i]}")
        #     print(f"current num: {num}")
        #     num += amount // coins[i]
        #     amount %= coins[i]
        #     i -= 1
        #     print(f"new amount: {amount}")
        #     print(f"new num: {num}")

        # if amount > 0:
        #     return -1

        # return num 
        
if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([186,419,83,408], 6249))