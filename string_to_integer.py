class Solution:
    def myAtoi(self, s: str) -> int:
        # print(s)
        if not s:
            return 0
        while s[0] == ' ':
            s = s[1:]
        if s[0] == '+':
            sign = 1
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0].isdigit():
            sign = 1
        else:
            print(s)
            return 2 / 0

        k = 0
        while k < len(s) and s[k].isdigit():
            k += 1
        s = s[:k]
        total = 0
        for i in range(k - 1, -1, -1):
            total += int(s[i]) * 10**(k - 1 - i)

        if sign == 1 and total >= 2**31:
            return 2**31
        elif sign == -1 and total > 2**31:
            return -2**31
        else:
            return total * sign


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi("   -42"))