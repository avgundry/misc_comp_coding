class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # attempt at DP. how can this be broken down..
        # let's see.
        # longest substring in s[:i], maybe?? 
        # maybe dp[i] holds the number of leftover left parens, and
        # otherwise longest valid substrings, in s[:i], as [left, len]
        # so for (()..dp = [[1, 0], [2, 0], [1, 2]]

        # then...let's say for ()((). We have:
        # dp = [[1, 0], [0, 2], [1, 2], [2, 2], [1, 2]]??
        #  But we have to see it's interrupted. Fuck; otherwise dp[-1] will be [1, 4].
        # This is where the issue lies.
        # maaaybe.



        # brute force...not quite there but close
        # holds the longest so far.
        longest = 0
        # how many left and right parentheses we've seen.
        left = right = 0


        # length of current substr

        curr_len = 0
        # the parens we've closed but can't add to list cause it's interrupted
        # by an unclosed one
        closed = 0
        for i in range(len(s)):
            curr = s[i]
            # if it's a right parentheses:
                # if we have no left one to match it, ignore
            if curr == ')':
                if left == 0:
                    curr_len = 0
                else:
                    left -= 1
                    closed += 1
            if curr == '(':
                left += 1
            if left == 0:
                curr_len += 2 * closed
                closed = 0
                    

            longest = max(longest, curr_len)

        return longest

if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")()())"))
    # should be 2.
    print(s.longestValidParentheses("()(()"))

