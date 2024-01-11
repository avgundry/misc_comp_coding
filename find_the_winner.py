class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """Brute force method: create an array and pop from it."""
        # Array of n friends.
        friends = [i for i in range(1, n + 1)]
        # Current index of the array.
        i = 0

        while len(friends) > 1:
            i = (i + k - 1) % len(friends)
            del friends[i]

        return friends[0]

if __name__ == "__main__":
    s = Solution()
    print(s.findTheWinner(5, 2))
        