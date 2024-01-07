# t0 = 0; t1 = 1; t2 = 1; t_{n+3} = t_n + t_{n+1} + t_{n+2} for n >= 0.

class Solution:
    def tribonacci(self, n: int) -> int:
        """Bottom-up DP solution"""
        arr = [0 for _ in range(n + 1)]
        arr[1] = arr[2] = 1
        for i in range(3, n+1):
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

        return arr[n]

if __name__ == "__main__":
    s = Solution()
    print(s.tribonacci(4))
    print(s.tribonacci(25))